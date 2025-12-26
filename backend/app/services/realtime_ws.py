import json
import logging
from typing import Any

from fastapi import WebSocket

from app.schemas.realtime_ws import (
    AudioPayload,
    ResponsePayload,
    StatusPayload,
    StreamEvent,
    TranscriptPayload,
)
from app.services.llm_client import LlmClient, LlmProviderError
from app.services.transcription import TranscriptionService
from app.services.tts_engine import TtsEngine

logger = logging.getLogger(__name__)


class RealtimeWsService:
    def __init__(
        self,
        transcription: TranscriptionService,
        llm_client: LlmClient,
        tts_engine: TtsEngine,
    ) -> None:
        self._transcription = transcription
        self._llm_client = llm_client
        self._tts_engine = tts_engine

    async def handle(self, websocket: WebSocket) -> None:
        token = websocket.headers.get("sec-websocket-protocol")
        await websocket.accept(subprotocol=token if token else None)
        await self._send_status(websocket, "recording")

        frames: list[bytes] = []
        try:
            while True:
                message = await websocket.receive()
                if message.get("bytes"):
                    frames.append(message["bytes"])
                    await self._send_transcript(websocket, text="", is_final=False)
                    continue
                if message.get("text"):
                    if _is_end_event(message["text"]):
                        break
                    await self._send_status(
                        websocket,
                        "error",
                        code="invalid_control",
                        message="Invalid control message",
                    )
                    break
        except Exception as exc:  # WebSocketDisconnect or unknown
            logger.info("realtime_ws_disconnect", extra={"error": str(exc)})
            return

        await self._process_frames(websocket, frames)

    async def _process_frames(self, websocket: WebSocket, frames: list[bytes]) -> None:
        try:
            await self._send_status(websocket, "transcribing")
            transcript = self._transcription.transcribe_stream(frames)
            await self._send_transcript(websocket, text=transcript.text, is_final=True)

            await self._send_status(websocket, "responding")
            response = self._llm_client.complete(transcript.text)
            await self._send_response(websocket, response.text)

            audio = self._tts_engine.synthesize(response.text, voice="default")
            await self._send_audio(websocket, audio.audio_format, audio.audio_bytes)
            await self._send_status(websocket, "idle")
        except ValueError as exc:
            code = "empty_stream" if str(exc) == "empty_stream" else "invalid_request"
            await self._send_status(websocket, "error", code=code, message=str(exc))
        except LlmProviderError as exc:
            await self._send_status(websocket, "error", code=exc.code, message=exc.message)
        except Exception as exc:
            await self._send_status(websocket, "error", code="unknown_error", message=str(exc))

    async def _send_status(
        self,
        websocket: WebSocket,
        state: str,
        code: str | None = None,
        message: str | None = None,
    ) -> None:
        payload = StatusPayload(state=state, code=code, message=message).model_dump()
        await self._send_event(websocket, "status", payload)

    async def _send_transcript(
        self,
        websocket: WebSocket,
        text: str,
        is_final: bool,
    ) -> None:
        payload = TranscriptPayload(text=text, is_final=is_final).model_dump()
        await self._send_event(websocket, "transcript", payload)

    async def _send_response(self, websocket: WebSocket, text: str) -> None:
        payload = ResponsePayload(text=text).model_dump()
        await self._send_event(websocket, "response", payload)

    async def _send_audio(self, websocket: WebSocket, fmt: str, data: bytes) -> None:
        payload = AudioPayload(format=fmt, size=len(data)).model_dump()
        await self._send_event(websocket, "audio", payload)
        await websocket.send_bytes(data)

    async def _send_event(self, websocket: WebSocket, event_type: str, payload: dict[str, Any]) -> None:
        event = StreamEvent(type=event_type, payload=payload).model_dump()
        await websocket.send_text(json.dumps(event))


def _is_end_event(message: str) -> bool:
    if message == '{"event": "end"}':
        return True
    try:
        data = json.loads(message)
    except json.JSONDecodeError:
        return False
    return data.get("event") == "end"
