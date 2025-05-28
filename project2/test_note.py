import unittest
from note import Note
from datetime import datetime
import re

class TestNote(unittest.TestCase):
    def test_initialization(self):
        note = Note(title="Test Title", content="Test Content")
        self.assertEqual(note.title, "Test Title")
        self.assertEqual(note.content, "Test Content")
        # Timestamp should be an ISO string: YYYY-MM-DDTHH:MM:SS
        self.assertTrue(re.match(r"\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}", note.timestamp))

    def test_to_dict(self):
        note = Note(title="Test Title", content="Test Content", timestamp="2022-01-01T12:34:56")
        note_dict = note.to_dict()
        expected = {
            "title": "Test Title",
            "content": "Test Content",
            "timestamp": "2022-01-01T12:34:56"
        }
        self.assertEqual(note_dict, expected)

    def test_from_dict(self):
        data = {
            "title": "Title X",
            "content": "Body X",
            "timestamp": "2023-04-05T14:22:00"
        }
        note = Note.from_dict(data)
        self.assertEqual(note.title, "Title X")
        self.assertEqual(note.content, "Body X")
        self.assertEqual(note.timestamp, "2023-04-05T14:22:00")

    def test_round_trip(self):
        note1 = Note(title="A", content="B")
        note2 = Note.from_dict(note1.to_dict())
        self.assertEqual(note1.title, note2.title)
        self.assertEqual(note1.content, note2.content)
        self.assertEqual(note1.timestamp, note2.timestamp)

if __name__ == '__main__':
    unittest.main()
