from pydantic import BaseModel, Field

from app.config import TTS_CONFIG


class TtsRequest(BaseModel):
    text: str = Field(min_length=1, max_length=TTS_CONFIG.max_text_length)
    voice: str = Field(default=TTS_CONFIG.default_voice)
