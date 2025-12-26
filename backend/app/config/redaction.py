SENSITIVE_KEYS = {
    "openai_api_key",
}


def is_sensitive(key: str) -> bool:
    return key in SENSITIVE_KEYS


def redact(value: str | None) -> str:
    if value is None:
        return ""
    return "****"
