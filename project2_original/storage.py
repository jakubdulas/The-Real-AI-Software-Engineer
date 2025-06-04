import json
from typing import List
from note import Note

def save_notes_to_file(notes: List[Note], filename: str) -> None:
    """
    Saves a list of Note instances to the specified JSON file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        data = [note.to_dict() for note in notes]
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_notes_from_file(filename: str) -> List[Note]:
    """
    Loads notes from the specified JSON file and returns a list of Note instances.
    If file does not exist or is empty, returns an empty list.
    """
    import os
    if not os.path.isfile(filename):
        return []
    with open(filename, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return []
        return [Note.from_dict(item) for item in data]
