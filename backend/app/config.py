from pydantic import BaseModel


class SttConfig(BaseModel):
    max_duration_seconds: int = 60
    supported_formats: tuple[str, ...] = ("wav", "flac", "mp3")


class LlmConfig(BaseModel):
    model: str = "gpt-5-mini"
    max_prompt_length: int = 4000


DEFAULT_CONFIG = SttConfig()
LLM_CONFIG = LlmConfig()
