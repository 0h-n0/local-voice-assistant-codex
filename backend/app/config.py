from pydantic import BaseModel


class SttConfig(BaseModel):
    max_duration_seconds: int = 60
    supported_formats: tuple[str, ...] = ("wav", "flac", "mp3")


class LlmConfig(BaseModel):
    model: str = "gpt-5-mini"
    max_prompt_length: int = 4000


class TtsConfig(BaseModel):
    max_text_length: int = 1000
    default_voice: str = "default"
    audio_format: str = "wav"


DEFAULT_CONFIG = SttConfig()
LLM_CONFIG = LlmConfig()
TTS_CONFIG = TtsConfig()
