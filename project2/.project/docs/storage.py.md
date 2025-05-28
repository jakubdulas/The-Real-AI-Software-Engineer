# `storage.py`

## Overview

The `storage.py` module manages the persistent storage of notes in a JSON file. It provides the `NoteStorage` class which encapsulates all CRUD (Create, Read, Update, Delete) operations on notes, handling serialization and deserialization between `Note` objects and their JSON representations.

---

## Module Responsibility
- Loads notes from and saves notes to a specified JSON file.
- Provides methods to retrieve, add, delete, update, and search notes.
- Isolates file I/O logic from the rest of the application.

---

## Classes

### `NoteStorage`
Handles all persistent storage of notes.

#### Attributes
- `filename` (`str`): Name of the file used for note storage (default: `notes.json`).
- `notes` (`List[Note]`): List of note objects loaded into memory.

#### Methods
- `__init__(self, filename: str = 'notes.json')`
    - Initialize storage, load notes if file exists, or start with empty list.
- `_load_from_file(self) -> None`
    - Internal. Loads and parses notes from disk.
    - Handles non-existent or malformed files gracefully (empties notes on error).
- `_save_to_file(self) -> None`
    - Internal. Writes current notes list to disk as JSON.
    - Raises `RuntimeError` on write failure.
- `get_all_notes(self) -> List[Note]`
    - Returns a (shallow) copy of all notes.
- `add_note(self, note: Note) -> None`
    - Appends a new note and saves.
- `delete_note(self, index: int) -> bool`
    - Deletes note at `index`. Returns `True` if successful, `False` if out of range.
- `update_note(self, index: int, new_note: Note) -> bool`
    - Replaces note at `index` with `new_note`. Returns `True` if successful.
- `find_note_by_title(self, title: str) -> Optional[Note]`
    - Locates note by its title. Returns the first match or `None` if not found.

---

## Typical Usage
```python
from storage import NoteStorage
from note import Note

storage = NoteStorage()
note = Note('Title', 'Body')
storage.add_note(note)
notes = storage.get_all_notes()
storage.delete_note(0)
```

---

## Developer Notes
- File read/write errors are handled silently (load) or as exceptions (save).
- Assumes that notes are manipulated by `Note` objects (see `note.py`).
- Used by the main UI logic (see `main.py`).
