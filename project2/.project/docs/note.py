"""
note.py
-------
Defines the Note class, representing a single note in the note manager.
Handles creation, serialization, and deserialization of notes.
"""
from datetime import datetime
from typing import Dict, Any

class Note:
    """
    Represents a single note with a title, content, and timestamp.

    Attributes:
        title (str): The title of the note.
        content (str): The content/body of the note.
        timestamp (str): The creation or last-modified timestamp (ISO 8601 format).
    """
    def __init__(self, title: str, content: str, timestamp: str = None) -> None:
        """
        Initialize a new Note instance.

        Args:
            title (str): Title of the note.
            content (str): Content/body of the note.
            timestamp (str, optional): Timestamp (ISO 8601 string), generated if not provided.
        """
        self.title = title
        self.content = content
        # If timestamp is not provided, use the current time in ISO format
        self.timestamp = timestamp if timestamp is not None else datetime.now().isoformat()

    def to_dict(self) -> Dict[str, Any]:
        """
        Serialize the Note object to a dictionary for JSON storage.

        Returns:
            dict: Serializable dictionary representing the note
        """
        return {
            'title': self.title,
            'content': self.content,
            'timestamp': self.timestamp
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'Note':
        """
        Create a Note object from a dictionary (reverse of to_dict).

        Args:
            data (dict): Dictionary with keys 'title', 'content', and 'timestamp'.
        Returns:
            Note: Instantiated Note object.
        """
        return Note(
            title=data['title'],
            content=data['content'],
            timestamp=data.get('timestamp')
        )
