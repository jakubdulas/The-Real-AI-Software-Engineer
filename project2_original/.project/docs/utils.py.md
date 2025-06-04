# utils.py

## Overview
`utils.py` includes general-purpose utility functions to support the note manager application. These helpers cover input validation, user confirmations, and human-friendly formatting for timestamps.

## Functions

### validate_non_empty(prompt)
- Prompts the user and ensures the input is not empty.
- Keeps prompting until a non-empty value is entered.

**Parameters:**
- `prompt` (str): The message to display for input.

**Returns:**
- `str`: The non-empty user input.

### format_timestamp(dt)
- Converts a datetime object or ISO 8601 timestamp string to a readable date/time string (`YYYY-MM-DD HH:MM:SS`).
- If given a string, attempts to parse it as an ISO-format date/time.

**Parameters:**
- `dt` (str | datetime): The timestamp to format.

**Returns:**
- `str`: Formatted timestamp or the original input if parsing fails.

### get_confirmation(prompt="Are you sure? (y/n): ")
- Asks the user for a yes/no confirmation.
- Only accepts 'y', 'yes', 'n', or 'no' (case-insensitive), keeps prompting otherwise.

**Parameters:**
- `prompt` (str): The message to display for confirmation. (Optional, default is "Are you sure? (y/n): ")

**Returns:**
- `bool`: `True` for yes, `False` for no.

## Usage Example
```python
from utils import validate_non_empty, format_timestamp, get_confirmation
value = validate_non_empty('Enter a title: ')
formatted = format_timestamp('2024-06-26T14:06:55')
if get_confirmation('Delete item? '):
    # proceed
    pass
```

## Dependencies
- `datetime` — Standard Python library for date parsing and formatting.

---
The module isolates common UI and conversion patterns to promote clean separation between user interaction and core logic.