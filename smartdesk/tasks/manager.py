from __future__ import annotations
from typing import List, Optional
from .models import Task
from .storage import JSONStorage


class TaskManager:
    def __init__(self, storage: Optional[JSONStorage] = None):
        self.storage = storage or JSONStorage()

    def create_task(self, title: str, description: str = "") -> Task:
        t = Task(title=title, description=description)
        self.storage.save_task(t)
        return t

    def list_tasks(self) -> List[Task]:
        return self.storage.list_tasks()
