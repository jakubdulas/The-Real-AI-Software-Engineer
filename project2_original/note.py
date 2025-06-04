from datetime import datetime
from typing import Dict, Any

class Note:
    """Class representing a note with title, content, and timestamp."""
    def __init__(self, title: str, content: str, timestamp: str = None) -> None:
        self.title = title
        self.content = content
        # If timestamp is not provided, use the current time in ISO format
        self.timestamp = timestamp if timestamp is not None else datetime.now().isoformat()

    def to_dict(self) -> Dict[str, Any]:
        """Serialize the note object to a dictionary for JSON storage."""
        return {
            'title': self.title,
            'content': self.content,
            'timestamp': self.timestamp
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'Note':
        """Create a Note object from a dictionary."""
        return Note(
            title=data['title'],
            content=data['content'],
            timestamp=data.get('timestamp')
        )
