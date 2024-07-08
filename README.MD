# FastAPI + htmx Project

This project is a simple FastAPI application integrated with htmx for building dynamic, interactive web pages. 
The project includes configurations for code formatting, linting, import sorting, and type checking using popular tools like `black`, `flake8`, `isort`, and `mypy`.

## Table of Contents

- [Getting Started](#getting-started)
- [Running the Project](#running-the-project)
- [Formatting Code](#formatting-code)
- [Linting Code](#linting-code)
- [Sorting Imports](#sorting-imports)
- [Type Checking](#type-checking)
- [Running Tests](#running-tests)


## Getting Started

### Prerequisites

- Python 3.9 or higher
- `pip` (Python package installer)

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/MichaelStaHelena/fastapi-htmx-experiments.git
   cd fastapi-htmx-experiments
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Project

To run the FastAPI application, use `fastapi dev`:

```bash
fastapi dev main.py --reload --port=8081
```

The application will be accessible at `http://127.0.0.1:8081`.

## Formatting Code

Install the tools:
```bash
pip install black flake8 flake8-pyproject isort mypy
```

This project uses `black` for code formatting. To format the code, run:

```bash
black .
```

## Linting Code

`flake8` is used for linting the code. To check for linting issues, run:

```bash
flake8 .
```

## Sorting Imports

`isort` is used to sort imports. To sort imports in the project, run:

```bash
isort .
```

## Type Checking

`mypy` is used for type checking. To check for type issues, run:

```bash
mypy .
```

## Running Tests

If you have tests, you can run them using `pytest`. To run tests, execute:

```bash
pytest
```
