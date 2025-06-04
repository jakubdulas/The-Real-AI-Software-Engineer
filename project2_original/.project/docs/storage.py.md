# storage.py

## Overview
`storage.py` handles persistent storage of notes by providing functions to load and save lists of `Note` objects to and from a JSON file. It ensures data integrity, error handling, and correct conversion between `Note` objects and their serializable form.

## Functions

### load_notes(filename: str) -> List[Note]
- Loads notes from a specified JSON file.
- Returns a list of `Note` objects.
- If the file does not exist, it returns an empty list.
- If the file is corrupted or cannot be loaded, it prints an error and returns an empty list.
- Handles exceptions such as `JSONDecodeError` and `IOError` gracefully.

**Parameters:**
- `filename` (str): The path to the JSON file where notes are stored.

**Returns:**
- `List[Note]`: A list of reconstructed `Note` objects.

### save_notes(filename: str, notes: List[Note]) -> None
- Saves a list of `Note` objects to the specified JSON file.
- Converts each note to a dictionary with `note.to_dict()` before dumping as JSON.
- Handles and reports I/O errors.

**Parameters:**
- `filename` (str): The path to the file for saving notes.
- `notes` (List[Note]): List of notes to be saved.

**Returns:**
- None

## Notes on Data Format
- The notes file is expected to be a list of dictionaries, each corresponding to a note, with keys 'title', 'content', and 'timestamp'.

## Usage Example
```python
from storage import load_notes, save_notes
notes = load_notes('notes.json')
# ... modify notes ...
save_notes('notes.json', notes)
```

## Dependencies
- `json` — For reading/writing JSON data.
- `os` — To check if files exist.
- `note.Note` — The Note class for object<->dict conversion.
- `typing` — For type hints.

---
The module keeps file I/O and object serialization concerns separated from logic and presentation. It is robust against file absence or corruption.