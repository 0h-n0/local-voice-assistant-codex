from fastapi import APIRouter, Depends, WebSocket

from app.services.llm_client import LlmClient
from app.services.realtime_ws import RealtimeWsService
from app.services.transcription import TranscriptionService
from app.services.tts_engine import TtsEngine

router = APIRouter()


def get_llm_client() -> LlmClient:
    return LlmClient()


def get_realtime_service(
    llm_client: LlmClient = Depends(get_llm_client),
) -> RealtimeWsService:
    return RealtimeWsService(
        transcription=TranscriptionService(),
        llm_client=llm_client,
        tts_engine=TtsEngine(),
    )


@router.websocket("/ws/voice")
async def realtime_voice(
    websocket: WebSocket,
    service: RealtimeWsService = Depends(get_realtime_service),
) -> None:
    await service.handle(websocket)
