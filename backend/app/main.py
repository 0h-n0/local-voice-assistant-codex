from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.api.health import router as health_router
from app.api.llm import router as llm_router
from app.api.orchestrator import router as orchestrator_router
from app.api.stt import router as stt_router
from app.api.tts import router as tts_router
from app.schemas.errors import ErrorResponse

app = FastAPI()
app.include_router(health_router)
app.include_router(llm_router)
app.include_router(orchestrator_router)
app.include_router(stt_router)
app.include_router(tts_router)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request, exc: RequestValidationError
) -> JSONResponse:
    return JSONResponse(
        status_code=400,
        content=ErrorResponse(code="validation_error", message="Invalid request").model_dump(),
    )
