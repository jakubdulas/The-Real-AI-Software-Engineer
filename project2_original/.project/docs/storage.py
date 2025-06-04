"""
storage.py
----------
Handles reading and writing the list of notes to a JSON file, using the Note class for serialization.
Provides functions to save notes and load notes from the persistent storage file.
"""
import json
from typing import List
from note import Note

def save_notes_to_file(notes: List[Note], filename: str) -> None:
    """
    Save a list of Note instances to the specified JSON file.

    Args:
        notes (list of Note): List of note instances to save.
        filename (str): Path to the JSON file to write to.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        data = [note.to_dict() for note in notes]
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_notes_from_file(filename: str) -> List[Note]:
    """
    Load notes from the specified JSON file and return a list of Note instances.
    If file does not exist or is empty, returns an empty list.

    Args:
        filename (str): Path to the JSON file to read.
    Returns:
        list of Note: List of notes loaded from file (empty if file missing or invalid).
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
