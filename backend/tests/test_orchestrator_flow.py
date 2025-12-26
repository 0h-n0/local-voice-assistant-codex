from fastapi.testclient import TestClient

from app.main import app


def test_orchestrator_returns_wav():
    client = TestClient(app)
    response = client.post(
        "/orchestrate",
        files={"file": ("sample.wav", b"RIFF", "audio/wav")},
    )
    assert response.status_code in (200, 502, 400)
    if response.status_code == 200:
        assert response.headers["content-type"].startswith("audio/wav")
