# Python Test Examples

This repository contains simple Python utility functions that are ideal for practicing test case writing. The code is intentionally kept simple and focused on data manipulation without any external dependencies or network calls.

## Project Structure

- `utils/`: Contains the main utility functions
  - `string_utils.py`: String manipulation functions
  - `math_utils.py`: Mathematical operations
  - `data_utils.py`: Data structure operations

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Unix/macOS
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Tests

To run tests:
```bash
pytest
```

To run tests with coverage:
```bash
pytest --cov=utils
```
