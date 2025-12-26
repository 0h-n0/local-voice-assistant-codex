from fastapi import APIRouter
from fastapi.responses import JSONResponse, Response

from app.schemas.errors import ErrorResponse
from app.schemas.tts import TtsRequest
from app.services.tts_engine import TtsEngine

router = APIRouter()
engine = TtsEngine()


@router.post(
    "/tts/synthesize",
    responses={400: {"model": ErrorResponse}, 500: {"model": ErrorResponse}},
)
async def synthesize(request: TtsRequest) -> Response:
    try:
        result = engine.synthesize(text=request.text, voice=request.voice)
    except ValueError as exc:
        if str(exc) == "unsupported_voice":
            return JSONResponse(
                status_code=400,
                content=ErrorResponse(
                    code="unsupported_voice",
                    message="Unsupported voice",
                ).model_dump(),
            )
        if str(exc) in {"empty_text", "text_too_long"}:
            return JSONResponse(
                status_code=400,
                content=ErrorResponse(code=str(exc), message="Invalid text").model_dump(),
            )
        return JSONResponse(
            status_code=500,
            content=ErrorResponse(code="tts_failed", message="TTS failed").model_dump(),
        )
    return Response(content=result.audio_bytes, media_type="audio/wav")
