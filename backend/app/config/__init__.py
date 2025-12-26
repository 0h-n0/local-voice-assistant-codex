"""Configuration helpers and resolved settings."""

from pydantic import BaseModel

from app.config.resolver import resolve_settings


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


class ConversationStorageConfig(BaseModel):
    database_path: str = "data/conversations.db"


_resolved = resolve_settings()
SETTINGS = _resolved.settings
CONFIG_SUMMARY = _resolved.entries

DEFAULT_CONFIG = SttConfig(
    max_duration_seconds=SETTINGS.stt_max_duration_seconds,
    supported_formats=tuple(SETTINGS.stt_supported_formats),
)
LLM_CONFIG = LlmConfig(
    model=SETTINGS.llm_model,
    max_prompt_length=SETTINGS.llm_max_prompt_length,
)
TTS_CONFIG = TtsConfig(
    max_text_length=SETTINGS.tts_max_text_length,
    default_voice=SETTINGS.tts_default_voice,
    audio_format=SETTINGS.tts_audio_format,
)
CONVERSATION_STORAGE_CONFIG = ConversationStorageConfig(
    database_path=SETTINGS.conversation_database_path
)

__all__ = [
    "CONFIG_SUMMARY",
    "CONVERSATION_STORAGE_CONFIG",
    "DEFAULT_CONFIG",
    "LLM_CONFIG",
    "SETTINGS",
    "TTS_CONFIG",
    "ConversationStorageConfig",
    "LlmConfig",
    "SttConfig",
    "TtsConfig",
]
