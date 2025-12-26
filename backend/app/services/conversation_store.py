from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import uuid4

from app.services.conversation_db import get_connection, init_db


@dataclass(frozen=True)
class ConversationSummary:
    id: str
    updated_at: str


@dataclass(frozen=True)
class MessageRecord:
    id: str
    role: str
    content: str
    created_at: str


@dataclass(frozen=True)
class ConversationDetail:
    id: str
    created_at: str
    updated_at: str
    messages: list[MessageRecord]


class ConversationStore:
    def __init__(self, database_path: str) -> None:
        self._database_path = database_path
        init_db(database_path)

    def append_messages(self, conversation_id: str, messages: list[dict]) -> ConversationDetail:
        if not messages:
            raise ValueError("empty_messages")
        now = _now_iso()
        with get_connection(self._database_path) as conn:
            existing = conn.execute(
                "SELECT id, created_at FROM conversations WHERE id = ?",
                (conversation_id,),
            ).fetchone()
            if existing:
                created_at = existing["created_at"]
            else:
                created_at = now
                conn.execute(
                    "INSERT INTO conversations (id, created_at, updated_at) VALUES (?, ?, ?)",
                    (conversation_id, created_at, now),
                )

            for message in messages:
                conn.execute(
                    "INSERT INTO messages (id, conversation_id, role, content, created_at) "
                    "VALUES (?, ?, ?, ?, ?)",
                    (
                        str(uuid4()),
                        conversation_id,
                        message["role"],
                        message["content"],
                        now,
                    ),
                )

            conn.execute(
                "UPDATE conversations SET updated_at = ? WHERE id = ?",
                (now, conversation_id),
            )

        return self.get_conversation(conversation_id)

    def get_conversation(self, conversation_id: str) -> ConversationDetail:
        with get_connection(self._database_path) as conn:
            convo = conn.execute(
                "SELECT id, created_at, updated_at FROM conversations WHERE id = ?",
                (conversation_id,),
            ).fetchone()
            if convo is None:
                raise KeyError("conversation_not_found")

            rows = conn.execute(
                "SELECT id, role, content, created_at FROM messages "
                "WHERE conversation_id = ? ORDER BY created_at ASC",
                (conversation_id,),
            ).fetchall()
            messages = [
                MessageRecord(
                    id=row["id"],
                    role=row["role"],
                    content=row["content"],
                    created_at=row["created_at"],
                )
                for row in rows
            ]

        return ConversationDetail(
            id=convo["id"],
            created_at=convo["created_at"],
            updated_at=convo["updated_at"],
            messages=messages,
        )

    def list_conversations(self) -> list[ConversationSummary]:
        with get_connection(self._database_path) as conn:
            rows = conn.execute(
                "SELECT id, updated_at FROM conversations ORDER BY updated_at DESC"
            ).fetchall()
        return [
            ConversationSummary(id=row["id"], updated_at=row["updated_at"]) for row in rows
        ]

    def delete_conversation(self, conversation_id: str) -> bool:
        with get_connection(self._database_path) as conn:
            row = conn.execute(
                "SELECT id FROM conversations WHERE id = ?",
                (conversation_id,),
            ).fetchone()
            if row is None:
                return False
            conn.execute("DELETE FROM conversations WHERE id = ?", (conversation_id,))
        return True


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()
