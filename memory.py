"""Small SQLite-backed conversation memory."""

import sqlite3
from pathlib import Path
from typing import Any


class Memory:
    def __init__(self, database_path: str = "agent_memory.sqlite3") -> None:
        self.database_path = database_path
        Path(database_path).parent.mkdir(parents=True, exist_ok=True) if Path(database_path).parent != Path(".") else None
        with self._connect() as connection:
            connection.execute(
                """CREATE TABLE IF NOT EXISTS messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT NOT NULL,
                    role TEXT NOT NULL CHECK(role IN ('user', 'assistant')),
                    content TEXT NOT NULL,
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                )"""
            )
            connection.execute(
                "CREATE INDEX IF NOT EXISTS idx_messages_user_id_id ON messages(user_id, id)"
            )

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row
        return connection

    def add(self, user_id: str, role: str, content: str) -> None:
        with self._connect() as connection:
            connection.execute(
                "INSERT INTO messages(user_id, role, content) VALUES (?, ?, ?)",
                (user_id, role, content),
            )

    def get_recent(self, user_id: str, limit: int = 10) -> list[dict[str, Any]]:
        with self._connect() as connection:
            rows = connection.execute(
                """SELECT role, content FROM (
                       SELECT id, role, content FROM messages
                       WHERE user_id = ? ORDER BY id DESC LIMIT ?
                   ) ORDER BY id ASC""",
                (user_id, limit),
            ).fetchall()
        return [{"role": row["role"], "content": row["content"]} for row in rows]

    def clear(self, user_id: str) -> None:
        with self._connect() as connection:
            connection.execute("DELETE FROM messages WHERE user_id = ?", (user_id,))
