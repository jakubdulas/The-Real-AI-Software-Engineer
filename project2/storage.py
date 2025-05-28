from typing import List
from note import Note
import json


def save_notes_to_file(notes: List[Note], filename: str) -> None:
    """
    Serialize and save list of Note objects to a JSON file.
    Args:
        notes: List of Note objects to save.
        filename: Path to the JSON file.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json_list = [note.to_dict() for note in notes]
            json.dump(json_list, f, indent=4)
    except Exception as e:
        print(f"Failed to save notes: {e}")


def load_notes_from_file(filename: str) -> List[Note]:
    """
    Load and deserialize list of Note objects from a JSON file.
    Args:
        filename: Path to the JSON file.
    Returns:
        List of Note objects.
    """
    notes = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for note_dict in data:
                notes.append(Note.from_dict(note_dict))
    except FileNotFoundError:
        # If file doesn't exist, return empty list
        pass
    except json.JSONDecodeError:
        print(f"Warning: '{filename}' contains invalid JSON. Returning empty note list.")
    except Exception as e:
        print(f"Failed to load notes: {e}")
    return notes
