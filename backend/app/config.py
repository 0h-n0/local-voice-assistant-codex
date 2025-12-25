from pydantic import BaseModel


class SttConfig(BaseModel):
    max_duration_seconds: int = 60
    supported_formats: tuple[str, ...] = ("wav", "flac", "mp3")


DEFAULT_CONFIG = SttConfig()
