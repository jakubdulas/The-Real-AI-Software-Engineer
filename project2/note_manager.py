"""
note_manager.py
---------------
Business logic for Note Manager: operations for note creation, loading, saving, and listing.
No user interaction/print/input here.
"""
from note import Note
from storage import save_notes_to_file, load_notes_from_file
from utils import validate_input, format_timestamp
from typing import List, Optional
import os

NOTES_FILE = 'notes.json'

def load_all_notes() -> List[Note]:
    return load_notes_from_file(NOTES_FILE)

def save_all_notes(notes: List[Note]):
    save_notes_to_file(notes, NOTES_FILE)

def create_note_logic(title: str, content: str) -> Optional[str]:
    """
    Business logic for creating a new note, validates and returns error message or None if ok.
    Returns error message string if input invalid or exception, otherwise saves note and returns None.
    """
    note_data = {'title': title, 'content': content}
    if not validate_input(note_data, ['title', 'content']):
        return "Title and content must not be empty."
    try:
        note = Note(title=title, content=content)
    except ValueError as ve:
        return str(ve)
    notes = load_all_notes()
    notes.append(note)
    save_all_notes(notes)
    return None

def get_notes_summaries() -> List[dict]:
    """
    Return a list of note summaries for UI display (index, title, timestamp).
    """
    notes = load_all_notes()
    results = []
    for idx, note in enumerate(notes, 1):
        results.append({
            'index': idx,
            'title': note.title,
            'timestamp': note.timestamp
        })
    return results

def get_note_detail(index: int) -> Optional[Note]:
    """
    Returns the Note object at (zero-based) index, or None if not found.
    """
    notes = load_all_notes()
    if 0 <= index < len(notes):
        return notes[index]
    return None
