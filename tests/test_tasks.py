from pathlib import Path

from smartdesk.tasks.manager import TaskManager
from smartdesk.tasks.storage import JSONStorage


def test_create_and_list_task(tmp_path):
    p = tmp_path / "tasks.json"
    storage = JSONStorage(path=p)
    manager = TaskManager(storage=storage)
    t = manager.create_task(title="Test task", description="desc")
    tasks = manager.list_tasks()
    assert any(x.id == t.id for x in tasks)
