from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import List
from pathlib import Path
import csv
import json

STORAGE = Path.home() / ".smartdesk" / "expenses.json"
STORAGE.parent.mkdir(parents=True, exist_ok=True)


@dataclass
class Expense:
    amount: float
    category: str
    date: datetime = field(default_factory=datetime.utcnow)
    note: str = ""


class ExpenseManager:
    def __init__(self, path: Path = STORAGE):
        self.path = path
        if not self.path.exists():
            self._write([])

    def _read(self):
        with self.path.open("r", encoding="utf8") as fh:
            return json.load(fh)

    def _write(self, data):
        with self.path.open("w", encoding="utf8") as fh:
            json.dump(data, fh, default=str, indent=2)

    def add_expense(self, amount: float, category: str = "misc", note: str = ""):
        raw = self._read()
        raw.append({
            "amount": float(amount),
            "category": category,
            "date": datetime.utcnow().isoformat(),
            "note": note,
        })
        self._write(raw)

    def list_expenses(self):
        raw = self._read()
        return raw

    def export_csv(self, out_path: Path):
        raw = self._read()
        with out_path.open("w", newline="", encoding="utf8") as fh:
            writer = csv.DictWriter(fh, fieldnames=["amount", "category", "date", "note"])
            writer.writeheader()
            writer.writerows(raw)
