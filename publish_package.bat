@echo off
REM ==============================
REM Activate venv, Test, Lint, Build, and Upload Python Package
REM ==============================

REM 1. Activate existing virtual environment
CALL venv\Scripts\activate.bat

REM 2. Upgrade pip
python -m pip install --upgrade pip

REM 3. Install/upgrade required packages
python -m pip install --upgrade build twine pytest flake8

REM 4. Lint code
echo Running code linting...
python -m flake8 .
IF ERRORLEVEL 1 (
    echo Linting failed. Fix errors before proceeding.
    EXIT /B 1
)

REM 5. Run tests
echo Running tests...
python -m pytest
IF ERRORLEVEL 1 (
    echo Tests failed. Fix tests before proceeding.
    EXIT /B 1
)

REM 6. Build the package
echo Building package...
python -m build
IF ERRORLEVEL 1 (
    echo Build failed.
    EXIT /B 1
)

REM 7. Upload package
IF "%PYPI_ENV%"=="prod" (
    echo Uploading to PyPI...
    python -m twine upload dist/*
) ELSE (
    echo Uploading to TestPyPI...
    python -m twine upload --repository testpypi dist/*
)

IF ERRORLEVEL 1 (
    echo Upload failed. Check credentials or version number.
    EXIT /B 1
)

echo All steps completed successfully!
pause
