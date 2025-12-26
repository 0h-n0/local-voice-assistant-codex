from fastapi.testclient import TestClient

from app.main import app


def test_config_summary_redacts_sensitive(monkeypatch, tmp_path):
    config_path = tmp_path / "config.toml"
    config_path.write_text("")
    monkeypatch.setenv("CONFIG_FILE", str(config_path))
    monkeypatch.setenv("OPENAI_API_KEY", "secret")

    client = TestClient(app)
    response = client.get("/config")

    assert response.status_code == 200
    payload = response.json()
    settings = {entry["key"]: entry for entry in payload["settings"]}
    assert settings["openai_api_key"]["value"] == "****"
    assert settings["openai_api_key"]["source"] == "env"
