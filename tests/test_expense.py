from pathlib import Path

from smartdesk.finance.expense_manager import ExpenseManager


def test_add_expense(tmp_path):
    p = tmp_path / "expenses.json"
    manager = ExpenseManager(path=p)
    manager.add_expense(amount=10.0, category="food", note="lunch")
    data = manager.list_expenses()
    assert len(data) == 1
    assert data[0]["category"] == "food"
