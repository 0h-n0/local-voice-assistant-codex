import json

from fastapi.testclient import TestClient

from app.api.realtime_ws import get_llm_client
from app.main import app
from app.services.llm_client import LlmResult


class FakeClient:
    def complete(self, prompt: str) -> LlmResult:
        return LlmResult(text="ok", model="test")


def test_realtime_status_events():
    app.dependency_overrides[get_llm_client] = lambda: FakeClient()
    client = TestClient(app)
    with client.websocket_connect("/ws/voice") as websocket:
        websocket.send_bytes(b"frame")
        websocket.send_text(json.dumps({"event": "end"}))

        states = []
        while True:
            message = websocket.receive()
            if message.get("text"):
                payload = json.loads(message["text"])
                if payload["type"] == "status":
                    states.append(payload["payload"]["state"])
                if payload["type"] == "status" and payload["payload"]["state"] == "idle":
                    break

        assert "recording" in states
        assert "transcribing" in states
        assert "responding" in states
        assert "idle" in states
    app.dependency_overrides.clear()
