from datetime import datetime
from typing import Dict, List, Any

def validate_input(data: Dict[str, Any], required_fields: List[str]) -> bool:
    """
    Validate that all required fields are present and non-empty in the data dict.

    Args:
        data (Dict[str, Any]): Input data to validate.
        required_fields (List[str]): Keys that must exist and be non-empty in data.
    Returns:
        bool: True if all fields are valid, False otherwise.
    """
    for field in required_fields:
        if field not in data or data[field] is None or (isinstance(data[field], str) and not data[field].strip()):
            return False
    return True

def format_timestamp(dt: datetime) -> str:
    """
    Format a datetime object into a human-readable timestamp string.

    Args:
        dt (datetime): The datetime object to format.
    Returns:
        str: Formatted timestamp string (e.g., '2024-06-07 14:03:02').
    """
    return dt.strftime('%Y-%m-%d %H:%M:%S')
