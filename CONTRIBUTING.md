# Contributing to SmartDesk

Thanks for your interest in contributing! By contributing to SmartDesk you agree to follow
the code of conduct and contribution guidelines below.

## How to contribute
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Make changes and add tests where applicable.
4. Run tests and linters locally:
   ```bash
   pre-commit run --all-files
   pytest
   ```
5. Commit and push to your fork and open a Pull Request.

## Code style
- We use `black`, `isort`, and `flake8`. Pre-commit hooks are configured.
- Use type annotations and docstrings for public functions/classes.
- Keep functions small and modular.

## Reporting security issues
Do NOT create public issues containing sensitive information (API keys, passwords, etc).
If you find a security vulnerability, contact the repository owner privately.

