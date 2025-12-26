from __future__ import annotations

from pathlib import Path
from typing import Any


def load_toml_config(path: str) -> dict[str, Any]:
    if not path:
        return {}
    config_path = Path(path)
    if not config_path.exists():
        return {}
    try:
        data = config_path.read_bytes()
        return _parse_toml_bytes(data)
    except OSError as exc:
        raise ValueError("config_unreadable") from exc


def load_dotenv_values(path: str = ".env") -> dict[str, str]:
    env_path = Path(path)
    if not env_path.exists():
        return {}
    values: dict[str, str] = {}
    for raw_line in env_path.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key:
            values[key] = value
    return values


def flatten_toml_config(data: dict[str, Any]) -> dict[str, Any]:
    mapping: dict[str, Any] = {}
    llm = data.get("llm", {})
    if "api_key" in llm:
        mapping["openai_api_key"] = llm.get("api_key")
    if "model" in llm:
        mapping["llm_model"] = llm.get("model")
    if "max_prompt_length" in llm:
        mapping["llm_max_prompt_length"] = llm.get("max_prompt_length")

    stt = data.get("stt", {})
    if "model_path" in stt:
        mapping["stt_model_path"] = stt.get("model_path")
    if "max_duration_seconds" in stt:
        mapping["stt_max_duration_seconds"] = stt.get("max_duration_seconds")
    if "supported_formats" in stt:
        mapping["stt_supported_formats"] = stt.get("supported_formats")

    tts = data.get("tts", {})
    if "model_path" in tts:
        mapping["tts_model_path"] = tts.get("model_path")
    if "max_text_length" in tts:
        mapping["tts_max_text_length"] = tts.get("max_text_length")
    if "default_voice" in tts:
        mapping["tts_default_voice"] = tts.get("default_voice")
    if "audio_format" in tts:
        mapping["tts_audio_format"] = tts.get("audio_format")

    audio = data.get("audio", {})
    if "input_device" in audio:
        mapping["audio_input_device"] = audio.get("input_device")
    if "output_device" in audio:
        mapping["audio_output_device"] = audio.get("output_device")

    storage = data.get("storage", {})
    if "database_path" in storage:
        mapping["conversation_database_path"] = storage.get("database_path")

    return mapping


def _parse_toml_bytes(data: bytes) -> dict[str, Any]:
    import tomllib

    try:
        return tomllib.loads(data.decode("utf-8"))
    except tomllib.TOMLDecodeError as exc:
        raise ValueError("config_malformed") from exc
