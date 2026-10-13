# Appium Learning Project

A beginner mobile test automation project using Python, Appium, and pytest.

## Tech Stack
- Python
- Appium-Python-Client
- pytest
- Android ApiDemos sample app

## Project Structure
- `conftest.py` - Shared Appium driver fixture
- `pages/` - Page Object Model classes
- `test_*.py` - Automated test cases
- `requirements.txt` - Python dependencies

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run Tests

Make sure the Appium server is running and the Android emulator is connected.

```bash
python -m pytest -v
```

## Learning Goals
- Mobile test automation with Appium
- Writing tests with pytest
- Using the Page Object Model
- Managing code with Git and GitHub