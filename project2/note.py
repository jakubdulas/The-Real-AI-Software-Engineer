from datetime import datetime
from typing import Dict, Any

class Note:
    def __init__(self, title: str, content: str, timestamp: str = None):
        self.title = title
        self.content = content
        # Use current timestamp if not provided
        if timestamp is None:
            self.timestamp = datetime.now().isoformat(sep=' ', timespec='seconds')
        else:
            self.timestamp = timestamp

    def to_dict(self) -> Dict[str, Any]:
        return {
            'title': self.title,
            'content': self.content,
            'timestamp': self.timestamp
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        return cls(
            title=data.get('title', ''),
            content=data.get('content', ''),
            timestamp=data.get('timestamp')
        )
