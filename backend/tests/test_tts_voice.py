from fastapi.testclient import TestClient

from app.main import app


def test_tts_unsupported_voice_returns_error():
    client = TestClient(app)
    response = client.post("/tts/synthesize", json={"text": "こんにちは", "voice": "alt"})
    assert response.status_code == 400
    payload = response.json()
    assert payload["code"] == "unsupported_voice"
