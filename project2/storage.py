import json
from typing import List, Optional
from note import Note
import os


class NoteStorage:
    """
    Handles CRUD operations for notes stored in a JSON file.
    """

    def __init__(self, filename: str = "notes.json"):
        self.filename = filename
        self.notes: List[Note] = []
        self._load_from_file()

    def _load_from_file(self) -> None:
        """
        Loads notes from the JSON file into memory.
        """
        try:
            if not os.path.exists(self.filename):
                self.notes = []
                return
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.notes = [Note.from_dict(note_dict) for note_dict in data]
        except (json.JSONDecodeError, IOError, TypeError, KeyError):
            self.notes = []  # start fresh on error

    def _save_to_file(self) -> None:
        """
        Saves the current list of notes to the JSON file.
        """
        try:
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump([note.to_dict() for note in self.notes], f, indent=2)
        except IOError as e:
            raise RuntimeError(f"Failed to save notes: {e}")

    def get_all_notes(self) -> List[Note]:
        return list(self.notes)

    def add_note(self, note: Note) -> None:
        self.notes.append(note)
        self._save_to_file()

    def delete_note(self, index: int) -> bool:
        if 0 <= index < len(self.notes):
            del self.notes[index]
            self._save_to_file()
            return True
        return False

    def update_note(self, index: int, new_note: Note) -> bool:
        if 0 <= index < len(self.notes):
            self.notes[index] = new_note
            self._save_to_file()
            return True
        return False

    def find_note_by_title(self, title: str) -> Optional[Note]:
        for note in self.notes:
            if note.title == title:
                return note
        return None
