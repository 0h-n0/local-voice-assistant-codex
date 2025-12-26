from typing import Literal

from pydantic import BaseModel


class StatusPayload(BaseModel):
    state: Literal["recording", "transcribing", "responding", "idle", "error"]
    code: str | None = None
    message: str | None = None


class TranscriptPayload(BaseModel):
    text: str
    is_final: bool


class ResponsePayload(BaseModel):
    text: str


class AudioPayload(BaseModel):
    format: str
    size: int


class StreamEvent(BaseModel):
    type: Literal["status", "transcript", "response", "audio"]
    payload: dict
