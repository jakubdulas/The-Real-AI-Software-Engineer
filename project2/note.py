from datetime import datetime
from typing import Dict, Any

class Note:
    """
    Represents a note with a title, content, and a timestamp.
    """
    def __init__(self, title: str, content: str, timestamp: str = None):
        self.title = title
        self.content = content
        # Timestamp should be ISO format string
        self.timestamp = timestamp or datetime.now().isoformat()

    def to_dict(self) -> Dict[str, Any]:
        """
        Serialize the Note instance to a dictionary.
        """
        return {
            'title': self.title,
            'content': self.content,
            'timestamp': self.timestamp
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Note':
        """
        Deserialize a dictionary to a Note instance.
        """
        return cls(
            title=data.get('title', ''),
            content=data.get('content', ''),
            timestamp=data.get('timestamp')
        )
