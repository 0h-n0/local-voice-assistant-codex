from typing import Literal

from pydantic import BaseModel, Field


class MessageCreate(BaseModel):
    role: Literal["user", "assistant", "system"]
    content: str = Field(min_length=1)


class AppendMessagesRequest(BaseModel):
    messages: list[MessageCreate]


class Message(BaseModel):
    id: str
    role: Literal["user", "assistant", "system"]
    content: str
    created_at: str


class ConversationSummary(BaseModel):
    id: str
    updated_at: str


class ConversationDetail(BaseModel):
    id: str
    created_at: str
    updated_at: str
    messages: list[Message]


class ConversationListResponse(BaseModel):
    conversations: list[ConversationSummary]
