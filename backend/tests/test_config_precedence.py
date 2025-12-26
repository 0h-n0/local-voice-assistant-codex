from app.config.resolver import resolve_settings


def test_precedence_env_over_dotenv_and_file(tmp_path, monkeypatch):
    config_path = tmp_path / "config.toml"
    config_path.write_text(
        """
[llm]
api_key="file-key"
model="file-model"
"""
    )
    dotenv_path = tmp_path / ".env"
    dotenv_path.write_text(
        """
OPENAI_API_KEY=dotenv-key
LLM_MODEL=dotenv-model
"""
    )

    monkeypatch.setenv("OPENAI_API_KEY", "env-key")

    resolved = resolve_settings(config_path=str(config_path), dotenv_path=str(dotenv_path))

    assert resolved.settings.openai_api_key == "env-key"
    assert resolved.source_map["openai_api_key"] == "env"
    assert resolved.settings.llm_model == "dotenv-model"
    assert resolved.source_map["llm_model"] == "dotenv"
