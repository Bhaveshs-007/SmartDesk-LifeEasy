from __future__ import annotations
import typer
from rich import print
from .tasks.manager import TaskManager
from .finance.expense_manager import ExpenseManager
from .info.weather import WeatherClient

app = typer.Typer(help="SmartDesk — Productivity Assistant")


@app.command()
def version():
    """Show package version."""
    from . import __version__
    print(f"[bold green]SmartDesk v{__version__}[/]")


@app.command()
def task_add(title: str = typer.Argument(...), description: str = typer.Option("", "-d")):
    """Add a task."""
    tm = TaskManager()
    task = tm.create_task(title=title, description=description)
    print(f"Created task: [cyan]{task.id}[/] {task.title}")


@app.command()
def task_list():
    """List tasks."""
    tm = TaskManager()
    tasks = tm.list_tasks()
    for t in tasks:
        print(f"- [{t.id}] {t.title} (completed={t.completed})")


@app.command()
def expense_add(amount: float = typer.Option(..., "--amount"), category: str = typer.Option("misc")):
    """Add expense."""
    em = ExpenseManager()
    em.add_expense(amount=amount, category=category)
    print(f"Expense added: {amount} under {category}")


@app.command()
def weather(city: str = typer.Option("London")):
    """Show current weather (requires API key)."""
    wc = WeatherClient()
    try:
        data = wc.current_weather(city)
        print(data)
    except Exception as exc:
        print(f"[red]Failed to fetch weather: {exc}[/]")


def main():
    app()


if __name__ == "__main__":
    main()
