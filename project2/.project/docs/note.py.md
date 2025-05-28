# note.py

## Module Purpose
The `note.py` module defines the core representation of a Note for the note manager application. It implements a flexible, easily serializable note class with input validation, providing the basis for creating, storing, and transmitting note objects throughout the app.

## Classes
### Note
Represents a single note, containing a title, content, and timestamp.

#### Attributes
- **title (str)**: The note's title. Required.
- **content (str)**: The body/content of the note. Required (can be empty string, but must be a string).
- **timestamp (str)**: The ISO-8601 formatted date/time the note was created or last modified.

#### Constructor
```python
Note(title: str, content: str, timestamp: Optional[str] = None)
```
- **title**: The title for the note. Must be a non-empty string.
- **content**: The note's content/body. Must be a string.
- **timestamp** (optional): If not provided, set to current datetime.

Raises `ValueError` if `title` is empty or `content` is not a string.

#### Methods
- `__repr__() -> str`
  - Returns a short string-representation suitable for debugging.
- `to_dict() -> Dict[str, Any]`
  - Serializes to a dict for easy storage/JSON conversion.
  - Returns: `{ 'title': ..., 'content': ..., 'timestamp': ... }`
- `@classmethod from_dict(data: Dict[str, Any]) -> Note`
  - Constructs a `Note` from dictionary data (e.g., parsed from JSON).
  - Expects at least 'title' and 'content'. 'timestamp' is optional.

#### Usage Example
```python
from note import Note
note = Note('Shopping List', 'Eggs, Milk', None)
data = note.to_dict()
restored = Note.from_dict(data)
```

---

