#!/usr/bin/env bash
set -e

echo "=============================================="
echo "SmartDesk Pre-Push Validation Script"
echo "=============================================="
echo

# Activate virtual environment
if [ -d "venv" ]; then
    echo "Activating virtual environment..."
    source venv/Scripts/activate
else
    echo "Virtual environment not found. Please create it first."
    exit 1
fi

echo
echo "Upgrading pip and installing dependencies..."
python -m pip install --upgrade pip > /dev/null 2>&1
pip install -r requirements.txt > /dev/null 2>&1

# Initialize result flags
BLACK_STATUS="Y"
ISORT_STATUS="Y"
FLAKE8_STATUS="Y"
PYTEST_STATUS="Y"

echo
echo "Running Black (code formatter)..."
if ! black . --check; then
    BLACK_STATUS="X"
fi

echo
echo "Running isort (import sorter)..."
if ! isort . --check-only; then
    ISORT_STATUS="X"
fi

echo
echo "Running Flake8 (linting)..."
if ! flake8 .; then
    FLAKE8_STATUS="X"
fi

echo
echo "Running Pytest (unit tests)..."
if ! pytest -v; then
    PYTEST_STATUS="X"
fi

echo
echo "=============================================="
echo "SUMMARY REPORT"
echo "=============================================="
printf "Black Formatter  : %s\n" "$BLACK_STATUS"
printf "isort Imports    : %s\n" "$ISORT_STATUS"
printf "Flake8 Linting   : %s\n" "$FLAKE8_STATUS"
printf "Pytest Tests     : %s\n" "$PYTEST_STATUS"
echo "=============================================="

if [[ "$BLACK_STATUS" == "Y" && "$ISORT_STATUS" == "Y" && "$FLAKE8_STATUS" == "Y" && "$PYTEST_STATUS" == "Y" ]]; then
    echo "All checks passed successfully! Safe to push "
    exit 0
else
    echo "Some checks failed. Please fix issues before pushing."
    exit 1
fi
