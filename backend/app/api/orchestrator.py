from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse, Response

from app.schemas.errors import ErrorResponse
from app.schemas.orchestrator import OrchestratorRequest
from app.services.orchestrator import OrchestratorService, StageFailure

router = APIRouter()
service = OrchestratorService()


@router.post(
    "/orchestrate",
    responses={400: {"model": ErrorResponse}, 502: {"model": ErrorResponse}},
)
async def orchestrate(file: UploadFile = File(...)) -> Response:
    audio_bytes = await file.read()
    request = OrchestratorRequest(audio_bytes=audio_bytes)
    try:
        result = service.run(request.audio_bytes)
    except StageFailure as exc:
        status = 400 if exc.stage == "stt" else 502
        return JSONResponse(
            status_code=status,
            content=ErrorResponse(code=exc.code, message=exc.message).model_dump(),
        )
    return Response(content=result.audio_bytes, media_type="audio/wav")
