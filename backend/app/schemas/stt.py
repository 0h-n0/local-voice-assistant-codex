from pydantic import BaseModel


class TranscriptionResult(BaseModel):
    request_id: str
    text: str
    language: str
    confidence: float
