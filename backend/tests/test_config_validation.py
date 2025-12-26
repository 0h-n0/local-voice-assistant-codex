import pytest

from app.config.resolver import ConfigValidationError, resolve_settings


def test_validation_error_on_invalid_value(tmp_path):
    dotenv_path = tmp_path / ".env"
    dotenv_path.write_text("LLM_MAX_PROMPT_LENGTH=not-an-int\n")

    with pytest.raises(ConfigValidationError) as excinfo:
        resolve_settings(config_path=str(tmp_path / "missing.toml"), dotenv_path=str(dotenv_path))

    fields = {issue.field for issue in excinfo.value.issues}
    assert "llm_max_prompt_length" in fields
