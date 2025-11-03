from dataclasses import dataclass, field
from datetime import datetime
import uuid
from typing import Optional


@dataclass
class Task:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    title: str = ""
    description: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    completed: bool = False
    completed_at: Optional[datetime] = None
