# utils.py

## Module Purpose
`utils.py` contains supplementary, reusable helper functions to support operations such as input validation and timestamp formatting, keeping logic clean and separate from domain objects and user interface.

## Functions

### validate_input
```python
def validate_input(data: Dict[str, Any], required_fields: List[str]) -> bool
```
- **data**: Dictionary of input data (e.g., from user input or a form)
- **required_fields**: List of keys that must exist in `data` and have non-empty values
- Returns: `True` if all required fields are present and valid, `False` otherwise
- Strings must be non-empty after stripping; non-string values must not be None.

#### Usage Example
```python
from utils import validate_input
inputs = {'title': 'T', 'content': 'X'}
validate_input(inputs, ['title', 'content'])   # True
validate_input({'title': ''}, ['title'])       # False
```

### format_timestamp
```python
def format_timestamp(dt: datetime) -> str
```
- **dt**: a `datetime` object
- Returns: a formatted string (e.g., `'2024-06-07 14:03:02'`)
- Used wherever human-readable timestamps are displayed.

#### Usage Example
```python
from utils import format_timestamp
from datetime import datetime
print(format_timestamp(datetime.now()))
```
