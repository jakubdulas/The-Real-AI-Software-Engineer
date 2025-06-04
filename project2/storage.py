import json
from typing import List
from note import Note
import os

def load_notes(filename: str) -> List[Note]:
    """Load notes from a JSON file. Return a list of Note objects."""
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Note.from_dict(note_data) for note_data in data]
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error loading notes: {e}")
        return []

def save_notes(filename: str, notes: List[Note]) -> None:
    """Save list of Note objects to a JSON file."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump([note.to_dict() for note in notes], f, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Error saving notes: {e}")
