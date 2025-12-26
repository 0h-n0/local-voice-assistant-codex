from __future__ import annotations

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_MAP = {
    "openai_api_key": "OPENAI_API_KEY",
    "llm_model": "LLM_MODEL",
    "llm_max_prompt_length": "LLM_MAX_PROMPT_LENGTH",
    "stt_model_path": "STT_MODEL_PATH",
    "stt_max_duration_seconds": "STT_MAX_DURATION_SECONDS",
    "stt_supported_formats": "STT_SUPPORTED_FORMATS",
    "tts_model_path": "TTS_MODEL_PATH",
    "tts_max_text_length": "TTS_MAX_TEXT_LENGTH",
    "tts_default_voice": "TTS_DEFAULT_VOICE",
    "tts_audio_format": "TTS_AUDIO_FORMAT",
    "audio_input_device": "AUDIO_INPUT_DEVICE",
    "audio_output_device": "AUDIO_OUTPUT_DEVICE",
    "conversation_database_path": "CONVERSATION_DATABASE_PATH",
    "config_file": "CONFIG_FILE",
}

REVERSE_ENV_MAP = {value: key for key, value in ENV_MAP.items()}


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_prefix="", extra="ignore", populate_by_name=True
    )

    openai_api_key: str | None = Field(default=None, alias=ENV_MAP["openai_api_key"])
    llm_model: str = Field(default="gpt-5-mini", alias=ENV_MAP["llm_model"])
    llm_max_prompt_length: int = Field(default=4000, alias=ENV_MAP["llm_max_prompt_length"])

    stt_model_path: str | None = Field(default=None, alias=ENV_MAP["stt_model_path"])
    stt_max_duration_seconds: int = Field(default=60, alias=ENV_MAP["stt_max_duration_seconds"])
    stt_supported_formats: list[str] = Field(
        default_factory=lambda: ["wav", "flac", "mp3"],
        alias=ENV_MAP["stt_supported_formats"],
    )

    tts_model_path: str | None = Field(default=None, alias=ENV_MAP["tts_model_path"])
    tts_max_text_length: int = Field(default=1000, alias=ENV_MAP["tts_max_text_length"])
    tts_default_voice: str = Field(default="default", alias=ENV_MAP["tts_default_voice"])
    tts_audio_format: str = Field(default="wav", alias=ENV_MAP["tts_audio_format"])

    audio_input_device: str | None = Field(default=None, alias=ENV_MAP["audio_input_device"])
    audio_output_device: str | None = Field(default=None, alias=ENV_MAP["audio_output_device"])

    conversation_database_path: str = Field(
        default="data/conversations.db", alias=ENV_MAP["conversation_database_path"]
    )

    config_file: str = Field(default="config.toml", alias=ENV_MAP["config_file"])
