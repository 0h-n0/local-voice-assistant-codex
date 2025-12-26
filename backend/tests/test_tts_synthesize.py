from fastapi.testclient import TestClient

from app.main import app


def test_tts_synthesize_returns_audio():
    client = TestClient(app)
    response = client.post("/tts/synthesize", json={"text": "こんにちは", "voice": "default"})
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("audio/wav")
    assert response.content
