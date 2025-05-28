"""
delete_note.py
-------------
Business logic helper for deleting a note by index.
"""
from note_manager import load_all_notes, save_all_notes
from typing import Optional

def delete_note_logic(index: int) -> Optional[str]:
    """
    Delete the note at the zero-based index. Returns None if successful, else error message.
    """
    notes = load_all_notes()
    if index < 0 or index >= len(notes):
        return "Invalid note index."
    removed = notes.pop(index)
    save_all_notes(notes)
    return None
