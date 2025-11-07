from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import List

from .models import Task

DEFAULT_STORAGE = Path.home() / ".smartdesk" / "tasks.json"
DEFAULT_STORAGE.parent.mkdir(parents=True, exist_ok=True)


class JSONStorage:
    def __init__(self, path: Path = DEFAULT_STORAGE):
        self.path = path
        if not self.path.exists():
            self._write([])

    def _read(self) -> List[dict]:
        with self.path.open("r", encoding="utf8") as fh:
            return json.load(fh)

    def _write(self, data: List[dict]):
        with self.path.open("w", encoding="utf8") as fh:
            json.dump(data, fh, default=str, indent=2)

    def save_task(self, task: Task):
        data = self._read()
        data.append(
            {
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "created_at": task.created_at.isoformat(),
                "completed": task.completed,
                "completed_at": (
                    task.completed_at.isoformat() if task.completed_at else None
                ),
            }
        )
        self._write(data)

    def list_tasks(self) -> List[Task]:
        raw = self._read()
        tasks = []
        for r in raw:
            t = Task(
                id=r["id"],
                title=r["title"],
                description=r.get("description", ""),
                created_at=datetime.fromisoformat(r["created_at"]),
                completed=r.get("completed", False),
                completed_at=(
                    datetime.fromisoformat(r["completed_at"])
                    if r.get("completed_at")
                    else None
                ),
            )
            tasks.append(t)
        return tasks
