import os
import json
from note import Note
import storage

TEST_FILE = 'test_notes.json'

def test_note_storage():
    # Cleanup before test
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    
    # Create test notes
    notes = [
        Note(title='Test1', content='Content1'),
        Note(title='Test2', content='Content2')
    ]
    
    # Save notes
    storage.save_notes_to_file(notes, TEST_FILE)
    assert os.path.exists(TEST_FILE)
    
    # Load notes
    loaded_notes = storage.load_notes_from_file(TEST_FILE)
    
    assert len(loaded_notes) == 2
    assert loaded_notes[0].title == 'Test1'
    assert loaded_notes[0].content == 'Content1'
    assert loaded_notes[1].title == 'Test2'
    assert loaded_notes[1].content == 'Content2'
    
    # Overwrite with empty list
    storage.save_notes_to_file([], TEST_FILE)
    loaded_notes = storage.load_notes_from_file(TEST_FILE)
    assert loaded_notes == []

    os.remove(TEST_FILE)
    print("test_note_storage PASSED")

if __name__ == '__main__':
    test_note_storage()
