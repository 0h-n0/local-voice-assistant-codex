from fastapi.testclient import TestClient

from app.api.conversations import get_conversation_store
from app.main import app
from app.services.conversation_store import ConversationStore


def test_delete_conversation_removes_history(tmp_path):
    store = ConversationStore(str(tmp_path / "conversations.db"))
    app.dependency_overrides[get_conversation_store] = lambda: store
    client = TestClient(app)

    client.post(
        "/conversations/conv-1/messages",
        json={"messages": [{"role": "user", "content": "Hello"}]},
    )

    response = client.delete("/conversations/conv-1")
    assert response.status_code == 204

    follow_up = client.get("/conversations/conv-1")
    assert follow_up.status_code == 404
    app.dependency_overrides.clear()


def test_delete_unknown_conversation_returns_not_found(tmp_path):
    store = ConversationStore(str(tmp_path / "conversations.db"))
    app.dependency_overrides[get_conversation_store] = lambda: store
    client = TestClient(app)

    response = client.delete("/conversations/missing")
    assert response.status_code == 404
    payload = response.json()
    assert payload["code"] == "not_found"
    app.dependency_overrides.clear()
