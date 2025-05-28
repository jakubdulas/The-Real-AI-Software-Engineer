# `note.py`

## Overview

The `note.py` module defines the core `Note` class used to represent a note within the note manager application. Each note instance encapsulates a title, content, and a timestamp, and provides serialization/deserialization methods for persistence and exchange with other modules.

---

## Module Responsibility
- Defines the `Note` data structure.
- Handles conversion between `Note` objects and serializable dictionaries.
- Provides easy integration with storage and user interface modules.

---

## Classes

### `Note`
Represents a single note with title, content, and timestamp.

#### Attributes
- `title` (`str`): The title of the note.
- `content` (`str`): The body/content of the note.
- `timestamp` (`str`): Creation timestamp in ISO 8601 format. If not specified, set to the current time.

#### Methods

- `__init__(self, title: str, content: str, timestamp: str = None)`
    - Initializes a new `Note` instance.
    - If `timestamp` is not given, default to current datetime (`datetime.now().isoformat()`).

- `to_dict(self) -> Dict[str, Any]`
    - Serializes this note to a dictionary suitable for JSON storage.
    - **Returns:** `dict` with keys `title`, `content`, `timestamp`.

- `@classmethod from_dict(cls, data: Dict[str, Any]) -> 'Note'`
    - Creates a `Note` instance from a dictionary (as loaded from storage).
    - Handles missing fields gracefully (default empty string for `title`/`content`).
    - **Arguments:**
        - `data`: Dictionary representation, e.g.: `{ 'title': ..., 'content': ..., 'timestamp': ... }`
    - **Returns:** `Note` object.

---

## Example Usage
```python
from note import Note
note = Note(title="Shopping List", content="Eggs, Milk, Bread")
note_dict = note.to_dict()
# Later...
restored_note = Note.from_dict(note_dict)
```

---

## Developer Notes
- Timestamp is always managed as an ISO-formatted string for cross-platform/date compatibility.
- Used by `storage.py` for persistence and in the main interface for display and manipulation.
