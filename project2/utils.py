"""
utils.py
General-purpose helper and validation functions for the note manager.
"""

def validate_non_empty_string(value: str) -> bool:
    """
    Validates that the input is a non-empty string (not just whitespace).

    Args:
        value (str): The string to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    return isinstance(value, str) and bool(value.strip())

def validate_menu_choice(choice: str, valid_options: list) -> bool:
    """
    Validates that a user menu choice is among the allowed options.

    Args:
        choice (str): User's menu input.
        valid_options (list): List of allowed option strings (e.g., ['1', '2', '3']).

    Returns:
        bool: True if valid, False otherwise.
    """
    return choice in valid_options

def validate_note_title(title: str) -> bool:
    """
    Validates the note title (non-empty, reasonably sized, trimmed).

    Args:
        title (str): The note title string.

    Returns:
        bool: True if valid, False otherwise.
    """
    return validate_non_empty_string(title) and len(title.strip()) <= 100

def validate_note_content(content: str) -> bool:
    """
    Validates note content (non-empty, trimmed, not excessively long).

    Args:
        content (str): The note content string.

    Returns:
        bool: True if valid, False otherwise.
    """
    return validate_non_empty_string(content) and len(content.strip()) <= 2000
