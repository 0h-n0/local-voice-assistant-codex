import json

from fastapi.testclient import TestClient

from app.api.realtime_ws import get_llm_client
from app.main import app
from app.services.llm_client import LlmResult


class FakeClient:
    def complete(self, prompt: str) -> LlmResult:
        return LlmResult(text="ok", model="test")


def test_realtime_stream_emits_partial_transcript():
    app.dependency_overrides[get_llm_client] = lambda: FakeClient()
    client = TestClient(app)
    with client.websocket_connect("/ws/voice", subprotocols=["local-token"]) as websocket:
        websocket.send_bytes(b"frame")
        websocket.send_text(json.dumps({"event": "end"}))

        partial_seen = False
        while True:
            message = websocket.receive()
            if message["type"] == "websocket.receive":
                continue
            if message.get("text"):
                payload = json.loads(message["text"])
                if payload["type"] == "transcript" and payload["payload"]["is_final"] is False:
                    partial_seen = True
                if payload["type"] == "status" and payload["payload"]["state"] == "idle":
                    break
            if message.get("bytes"):
                continue

        assert partial_seen
    app.dependency_overrides.clear()
