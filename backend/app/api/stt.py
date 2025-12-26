from fastapi import APIRouter, File, Form, UploadFile, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse

from app.schemas.errors import ErrorResponse
from app.schemas.stt import TranscriptionResult
from app.services.transcription import TranscriptionService

router = APIRouter()
service = TranscriptionService()


@router.post(
    "/stt/file",
    response_model=TranscriptionResult,
    responses={400: {"model": ErrorResponse}},
)
async def transcribe_file(
    file: UploadFile = File(...),
    audio_format: str = Form("wav"),
) -> TranscriptionResult:
    data = await file.read()
    try:
        output = service.transcribe_file(stream=data, audio_format=audio_format)
    except ValueError as exc:
        if str(exc) == "unsupported_audio_format":
            return JSONResponse(
                status_code=400,
                content=ErrorResponse(
                    code="unsupported_audio_format",
                    message="Unsupported audio format",
                ).model_dump(),
            )
        return JSONResponse(
            status_code=400,
            content=ErrorResponse(code="invalid_request", message="Invalid request").model_dump(),
        )
    return TranscriptionResult(
        request_id="req-file",
        text=output.text,
        language=output.language,
        confidence=output.confidence,
    )


@router.websocket("/stt/stream")
async def stt_stream(websocket: WebSocket) -> None:
    await websocket.accept()
    frames: list[bytes] = []
    try:
        while True:
            message = await websocket.receive()
            if "bytes" in message and message["bytes"]:
                frames.append(message["bytes"])
                continue
            if "text" in message and message["text"]:
                if message["text"] == '{"event": "end"}':
                    try:
                        output = service.transcribe_stream(frames)
                    except ValueError as exc:
                        if str(exc) == "empty_stream":
                            await websocket.send_json(
                                {
                                    "event": "error",
                                    "code": "empty_stream",
                                    "message": "No audio frames received",
                                }
                            )
                            break
                        await websocket.send_json(
                            {
                                "event": "error",
                                "code": "invalid_request",
                                "message": "Invalid stream request",
                            }
                        )
                        break
                    await websocket.send_json({"event": "final", "text": output.text})
                    break
                await websocket.send_json(
                    {
                        "event": "error",
                        "code": "invalid_control",
                        "message": "Invalid control message",
                    }
                )
    except WebSocketDisconnect:
        return
