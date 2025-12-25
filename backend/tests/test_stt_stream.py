from fastapi.testclient import TestClient

from app.main import app


def test_stream_returns_final_event():
    client = TestClient(app)
    with client.websocket_connect("/stt/stream") as websocket:
        websocket.send_bytes(b"audio")
        websocket.send_text('{"event": "end"}')
        data = websocket.receive_json()
    assert data["event"] == "final"
    assert "text" in data
