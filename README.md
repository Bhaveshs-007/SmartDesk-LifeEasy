# SmartDesk - Python Productivity Assistant

[![Build Status](https://github.com/<your-username>/smartdesk/actions/workflows/ci.yml/badge.svg)]()
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)]()
[![License: MIT](https://img.shields.io/badge/license-MIT-green)]()

SmartDesk is a modular command-line productivity assistant written in Python.
It helps manage tasks & notes, track expenses, fetch info (weather/news/stocks via APIs), and export reports.

---

## Features
- Task & note management (JSON or SQLite storage)
- Expense tracker with CSV export and simple visualizations
- Small API clients for weather/news/stocks (requires user-provided API keys)
- CLI implemented with Typer and Rich for nice CLI UX
- Unit tests with pytest, linting with flake8 + black
- Packaging ready (pyproject.toml / setup.py)
- GitHub Actions CI to run tests & lint on push/PR
- Optional: publish to PyPI on tag creation (workflow included; disabled by default)

---

## Quick start

```bash
git clone https://github.com/<your-username>/smartdesk.git
cd smartdesk
python3 -m venv venv
source venv/bin/activate         # Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m smartdesk.cli --help
```

To run tests:
```bash
pytest
```

To build package:
```bash
pip install build
python -m build
```

---

## Contributing
See `CONTRIBUTING.md` for contribution notes and code style.

## Security & Privacy
- Do not commit API keys or credentials to the repository. Use a local `.env` file (see `.env.example`) or environment variables.
- If you accidentally commit a secret, rotate it immediately and remove it from history.

---

## License
This project is released under the MIT License. See `LICENSE` for details.
