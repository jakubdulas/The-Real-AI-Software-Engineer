# note.py

## Overview
`note.py` defines the core `Note` class for the note manager project. This class represents an individual note, encapsulating its title, content, and creation timestamp. It also provides methods for turning notes into JSON-compatible dictionaries and reconstructing notes from such data.

## Classes and Functions

### class Note
Models a single note.

#### Attributes:
- **title** (`str`): The title of the note.
- **content** (`str`): The main text/content of the note.
- **timestamp** (`str`): When the note was created. By default, set to the current time, formatted as an ISO 8601 string (e.g., `'2024-06-26 13:12:05'`).

#### Methods:
- **__init__(self, title: str, content: str, timestamp: str = None)**
    - Creates a new Note instance.
    - If no timestamp is provided, it uses the current system time.
- **to_dict(self) -> Dict[str, Any]**
    - Returns a dictionary representation of the note, suitable for JSON serialization. Keys are `'title'`, `'content'`, and `'timestamp'`.
- **@classmethod from_dict(cls, data: Dict[str, Any])**
    - Reconstructs a Note from a dictionary (e.g. loaded from JSON). Handles missing fields by supplying defaults as necessary.

## Usage Example
```python
note = Note('Title', 'Content goes here')
note_dict = note.to_dict()
note2 = Note.from_dict(note_dict)
```

## Dependencies
- `datetime` — Standard Python library for handling timestamps.
- `typing` — For type hints.

---
This module contains only the data model and serialization logic; all persistence and input/output is handled outside of this module.