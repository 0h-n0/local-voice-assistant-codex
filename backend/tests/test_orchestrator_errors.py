from fastapi.testclient import TestClient

from app.main import app


def test_orchestrator_empty_audio_returns_error():
    client = TestClient(app)
    response = client.post(
        "/orchestrate",
        files={"file": ("empty.wav", b"", "audio/wav")},
    )
    assert response.status_code == 400
    payload = response.json()
    assert payload["code"] == "empty_audio"
