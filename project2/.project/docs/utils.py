"""
utils.py
--------
Provides various helper functions for validating and sanitizing user input, formatting timestamps, and validating menu choices.
Useful for input checking and data formatting in the note manager project.
"""
import re
from datetime import datetime

def is_empty_input(input_str: str) -> bool:
    """
    Check if the input string is empty after stripping whitespace.
    Args:
        input_str (str): The input string to validate.
    Returns:
        bool: True if empty, False otherwise.
    """
    return not input_str.strip()

def sanitize_string(input_str: str) -> str:
    """
    Sanitize the input string by removing leading/trailing whitespace
    and any potentially dangerous non-printable characters.
    Args:
        input_str (str): The string to sanitize.
    Returns:
        str: A sanitized version of the string.
    """
    # Remove non-printable/control characters
    sanitized = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', input_str)
    return sanitized.strip()

def format_timestamp(dt_str: str) -> str:
    """
    Format an ISO 8601 datetime string to a human-readable form.
    Args:
        dt_str (str): ISO 8601 formatted datetime string.
    Returns:
        str: Formatted timestamp for display.
    """
    try:
        dt = datetime.fromisoformat(dt_str)
        return dt.strftime('%Y-%m-%d %H:%M:%S')
    except Exception:
        return dt_str  # fallback to original if parsing fails

def validate_menu_choice(choice: str, valid_choices=("1", "2", "3", "4")) -> bool:
    """
    Validate that the menu choice is among valid options.
    Args:
        choice (str): User input selection.
        valid_choices (tuple): Valid option strings.
    Returns:
        bool: True if valid, False otherwise.
    """
    return choice in valid_choices

def validate_note_title(title: str) -> bool:
    """
    Validate that the note title is of acceptable length and not empty after sanitization.
    Args:
        title (str): Note title input.
    Returns:
        bool: True if title is valid.
    """
    title = sanitize_string(title)
    return bool(title) and len(title) <= 100

def sanitize_text(text: str) -> str:
    """
    Runs comprehensive sanitization on a text input for note content or title.
    Args:
        text (str): The text to sanitize.
    Returns:
        str: A clean string with unsafe chars removed and whitespace trimmed.
    """
    return sanitize_string(text)
