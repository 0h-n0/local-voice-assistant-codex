from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Any

from pydantic import ValidationError

from app.config.file_loader import (
    flatten_toml_config,
    load_dotenv_values,
    load_toml_config,
)
from app.config.redaction import is_sensitive, redact
from app.config.settings import AppSettings, ENV_MAP, REVERSE_ENV_MAP


@dataclass(frozen=True)
class ConfigIssue:
    field: str
    message: str


class ConfigValidationError(RuntimeError):
    def __init__(self, issues: list[ConfigIssue]) -> None:
        super().__init__("invalid_config")
        self.issues = issues


class ConfigLoadError(RuntimeError):
    def __init__(self, code: str) -> None:
        super().__init__(code)
        self.code = code


@dataclass(frozen=True)
class ConfigEntry:
    key: str
    value: str
    source: str
    sensitive: bool


@dataclass(frozen=True)
class ResolvedConfig:
    settings: AppSettings
    entries: list[ConfigEntry]
    source_map: dict[str, str]


def resolve_settings(config_path: str | None = None, dotenv_path: str = ".env") -> ResolvedConfig:
    dotenv_values = load_dotenv_values(dotenv_path)
    try:
        settings = AppSettings(_env_file=dotenv_path)
    except ValidationError as exc:
        raise ConfigValidationError(_format_validation_errors(exc)) from exc

    config_file = config_path or settings.config_file
    try:
        file_data = load_toml_config(config_file)
    except ValueError as exc:
        raise ConfigLoadError(str(exc)) from exc

    file_flat = flatten_toml_config(file_data)
    merged = settings.model_dump()

    for key, value in file_flat.items():
        if key not in settings.model_fields_set:
            merged[key] = value

    try:
        resolved = AppSettings.model_validate(merged)
    except ValidationError as exc:
        raise ConfigValidationError(_format_validation_errors(exc)) from exc

    source_map = _build_source_map(resolved, dotenv_values, file_flat)
    entries = _build_entries(resolved, source_map)
    return ResolvedConfig(settings=resolved, entries=entries, source_map=source_map)


def _format_validation_errors(exc: ValidationError) -> list[ConfigIssue]:
    issues: list[ConfigIssue] = []
    for err in exc.errors():
        loc = err.get("loc", [])
        raw_field = ".".join(str(part) for part in loc) or "unknown"
        field = REVERSE_ENV_MAP.get(raw_field, raw_field)
        msg = err.get("msg", "Invalid value")
        issues.append(ConfigIssue(field=field, message=msg))
    return issues


def _build_source_map(
    settings: AppSettings,
    dotenv_values: dict[str, str],
    file_flat: dict[str, Any],
) -> dict[str, str]:
    sources: dict[str, str] = {}
    for field, env_name in ENV_MAP.items():
        if env_name in os.environ:
            sources[field] = "env"
        elif env_name in dotenv_values:
            sources[field] = "dotenv"
        elif field in file_flat:
            sources[field] = "config_file"
        else:
            sources[field] = "default"
    return sources


def _build_entries(settings: AppSettings, source_map: dict[str, str]) -> list[ConfigEntry]:
    entries: list[ConfigEntry] = []
    for field in ENV_MAP.keys():
        value = getattr(settings, field)
        if isinstance(value, list):
            rendered = ",".join(str(item) for item in value)
        else:
            rendered = "" if value is None else str(value)
        sensitive = is_sensitive(field)
        entries.append(
            ConfigEntry(
                key=field,
                value=redact(rendered) if sensitive else rendered,
                source=source_map[field],
                sensitive=sensitive,
            )
        )
    return entries
