# storage.py

## Module Purpose
`storage.py` provides all functionality for saving notes to and loading notes from a persistent JSON file. It acts as an abstraction between the application logic and the underlying file system, handling serialization, error tolerance, and conversion between Note objects and their storage representations.

## Functions

### save_notes_to_file
```python
def save_notes_to_file(notes: List[Note], filename: str) -> None
```
- **notes**: List of `Note` objects to save.
- **filename**: Path/name of the JSON file to write.
- Serializes the notes (using `to_dict` for each) and writes to the file as JSON.
- Handles and prints errors that occur during the save operation.

### load_notes_from_file
```python
def load_notes_from_file(filename: str) -> List[Note]
```
- **filename**: Path/name of the JSON file to read from.
- Reads from the file and deserializes JSON into `Note` objects (using `Note.from_dict`).
- Returns:
    - A list of `Note` objects.
    - If the file doesn't exist, returns an empty list.
    - If the file contains invalid JSON, prints a warning and returns empty list.
    - Handles any unexpected errors gracefully, providing brief feedback via print.

## Usage Example
```python
from storage import save_notes_to_file, load_notes_from_file
from note import Note
notes = [Note('a', 'b'), Note('x', 'y')]
save_notes_to_file(notes, 'notes.json')
notes2 = load_notes_from_file('notes.json')
```
