from datetime import datetime
from typing import Dict, Any, Optional

class Note:
    """
    Represents a note containing a title, content, and a timestamp.

    Attributes:
        title (str): The title of the note.
        content (str): The body content of the note.
        timestamp (str): The ISO-formatted datetime string of note creation or last modification.
    """
    def __init__(self, title: str, content: str, timestamp: Optional[str] = None):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Title must be a non-empty string.")
        if not isinstance(content, str):
            raise ValueError("Content must be a string.")
        self.title = title
        self.content = content
        if timestamp is None:
            self.timestamp = datetime.now().isoformat(timespec='seconds')
        else:
            self.timestamp = timestamp

    def __repr__(self) -> str:
        return f"<Note(title={self.title!r}, timestamp={self.timestamp!r})>"

    def to_dict(self) -> Dict[str, Any]:
        """
        Serialize the Note instance to a dictionary.
        Returns:
            dict: Dictionary with keys 'title', 'content', and 'timestamp'.
        """
        return {
            "title": self.title,
            "content": self.content,
            "timestamp": self.timestamp
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Note':
        """
        Deserialize a Note instance from a dictionary.

        Args:
            data (dict): Dictionary containing keys 'title', 'content', and optionally 'timestamp'.

        Returns:
            Note: Corresponding Note instance.
        """
        return cls(
            title=data["title"],
            content=data["content"],
            timestamp=data.get("timestamp")
        )
