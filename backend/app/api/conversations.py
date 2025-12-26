import logging

from fastapi import APIRouter, Depends, Response
from fastapi.responses import JSONResponse

from app.config import CONVERSATION_STORAGE_CONFIG
from app.schemas.conversations import (
    AppendMessagesRequest,
    ConversationDetail,
    ConversationListResponse,
)
from app.schemas.errors import ErrorResponse
from app.services.conversation_store import ConversationStore

router = APIRouter()
logger = logging.getLogger(__name__)


def get_conversation_store() -> ConversationStore:
    return ConversationStore(CONVERSATION_STORAGE_CONFIG.database_path)


@router.get(
    "/conversations",
    response_model=ConversationListResponse,
)
async def list_conversations(
    store: ConversationStore = Depends(get_conversation_store),
) -> ConversationListResponse:
    conversations = store.list_conversations()
    return ConversationListResponse(
        conversations=[c.__dict__ for c in conversations],
    )


@router.get(
    "/conversations/{conversation_id}",
    response_model=ConversationDetail,
    responses={404: {"model": ErrorResponse}},
)
async def get_conversation(
    conversation_id: str,
    store: ConversationStore = Depends(get_conversation_store),
) -> ConversationDetail | JSONResponse:
    try:
        convo = store.get_conversation(conversation_id)
    except KeyError:
        return JSONResponse(
            status_code=404,
            content=ErrorResponse(code="not_found", message="Conversation not found").model_dump(),
        )
    return ConversationDetail(
        id=convo.id,
        created_at=convo.created_at,
        updated_at=convo.updated_at,
        messages=[m.__dict__ for m in convo.messages],
    )


@router.post(
    "/conversations/{conversation_id}/messages",
    response_model=ConversationDetail,
    responses={400: {"model": ErrorResponse}},
)
async def append_messages(
    conversation_id: str,
    request: AppendMessagesRequest,
    store: ConversationStore = Depends(get_conversation_store),
) -> ConversationDetail | JSONResponse:
    logger.info(
        "conversation_append_request",
        extra={"conversation_id": conversation_id, "count": len(request.messages)},
    )
    try:
        convo = store.append_messages(conversation_id, [m.model_dump() for m in request.messages])
    except ValueError:
        return JSONResponse(
            status_code=400,
            content=ErrorResponse(
                code="empty_messages",
                message="At least one message is required",
            ).model_dump(),
        )
    return ConversationDetail(
        id=convo.id,
        created_at=convo.created_at,
        updated_at=convo.updated_at,
        messages=[m.__dict__ for m in convo.messages],
    )


@router.delete(
    "/conversations/{conversation_id}",
    response_class=Response,
    response_model=None,
    responses={
        204: {"description": "Deleted"},
        404: {"model": ErrorResponse},
    },
)
async def delete_conversation(
    conversation_id: str,
    store: ConversationStore = Depends(get_conversation_store),
) -> Response:
    removed = store.delete_conversation(conversation_id)
    if not removed:
        return JSONResponse(
            status_code=404,
            content=ErrorResponse(code="not_found", message="Conversation not found").model_dump(),
        )
    return Response(status_code=204)
