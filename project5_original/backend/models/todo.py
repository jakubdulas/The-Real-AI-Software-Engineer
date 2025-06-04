from typing import Optional
from datetime import date

class TodoItem:
    def __init__(self, id: int, title: str, done: bool = False, due_date: Optional[date] = None):
        self.id = id
        self.title = title
        self.done = done
        self.due_date = due_date

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'done': self.done,
            'due_date': self.due_date.isoformat() if self.due_date else None,
        }
