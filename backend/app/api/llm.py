import logging

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.schemas.errors import ErrorResponse
from app.schemas.llm import LlmRequest, LlmResponse
from app.services.llm_client import LlmClient, LlmProviderError

router = APIRouter()
logger = logging.getLogger(__name__)


def get_llm_client() -> LlmClient:
    return LlmClient()


@router.post(
    "/llm/complete",
    response_model=LlmResponse,
    responses={
        400: {"model": ErrorResponse},
        502: {"model": ErrorResponse},
        500: {"model": ErrorResponse},
    },
)
async def complete(
    request: LlmRequest,
    client: LlmClient = Depends(get_llm_client),
) -> LlmResponse | JSONResponse:
    logger.info("llm_request_received", extra={"prompt_length": len(request.prompt)})
    try:
        result = client.complete(request.prompt)
    except LlmProviderError as exc:
        status = 502 if exc.code == "provider_error" else 500
        return JSONResponse(
            status_code=status,
            content=ErrorResponse(code=exc.code, message=exc.message).model_dump(),
        )
    return LlmResponse(request_id="req-llm", text=result.text, model=result.model)
