# `utils.py`

## Overview

The `utils.py` module provides general-purpose helper and validation functions for the note manager application. These utilities are used throughout the codebase to ensure user inputs meet the requirements for note titles, contents, and menu selections.

---

## Module Responsibility
- Encapsulates input validation logic for note data and menu interaction.
- Simplifies and standardizes input checking across UI and logic modules.

---

## Functions

### `validate_non_empty_string(value: str) -> bool`
Checks that the provided value is a non-empty string (non-blank, not just whitespace).

- **Args:**
  - `value` (`str`): The string to check.
- **Returns:**
  - `bool`: `True` if valid, `False` otherwise.

### `validate_menu_choice(choice: str, valid_options: list) -> bool`
Checks that a menu choice from user input is among the permitted options.

- **Args:**
  - `choice` (`str`): Input from user.
  - `valid_options` (`list`): Allowed string values (e.g., `["1","2"]`).
- **Returns:**
  - `bool`: `True` if `choice` is in `valid_options`.

### `validate_note_title(title: str) -> bool`
Validates a note title. Title must be non-empty (not just whitespace) and up to 100 characters.

- **Args:**
  - `title` (`str`): Note title string from user input.
- **Returns:**
  - `bool`: `True` if valid, `False` otherwise.

### `validate_note_content(content: str) -> bool`
Validates note content string to be non-empty and up to 2000 characters.

- **Args:**
  - `content` (`str`): Note body/content string.
- **Returns:**
  - `bool`: `True` if valid, `False` otherwise.

---

## Example Usage
```python
from utils import validate_menu_choice, validate_note_title, validate_note_content

# Validate a menu input
if validate_menu_choice(user_choice, ["1", "2", "3"]):
    ...

# Title/content validation
if validate_note_title(title) and validate_note_content(content):
    ...
```

## Developer Notes
- Used throughout the user interface (in `main.py`) for robust input checking.
- Keeping validations in a separate module supports testability and easy updates to rules.
