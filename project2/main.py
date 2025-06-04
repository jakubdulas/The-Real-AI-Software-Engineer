import sys
from note import Note
from storage import load_notes, save_notes
from utils import validate_non_empty, get_confirmation, format_timestamp

NOTES_FILE = 'notes.json'

def display_menu():
    print("\n--- Command Line Note Manager ---")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Delete Note")
    print("4. Exit")
    
def prompt_choice():
    while True:
        choice = input("Select an option (1-4): ").strip()
        if choice in {'1', '2', '3', '4'}:
            return choice
        print("Invalid input. Please enter a number between 1 and 4.")

def add_note(notes):
    print("\n--- Add Note ---")
    title = validate_non_empty(input("Title: "), "Title cannot be empty.")
    content = validate_non_empty(input("Content: "), "Content cannot be empty.")
    note = Note(title=title, content=content)
    notes.append(note)
    save_notes(NOTES_FILE, notes)
    print("Note added!")

def view_notes(notes):
    print("\n--- Notes ---")
    if not notes:
        print("No notes available.")
        return
    for idx, note in enumerate(notes, start=1):
        print(f"{idx}. [{format_timestamp(note.timestamp)}] {note.title}")
    detail = input("\nEnter note number to view details, or press Enter to return: ").strip()
    if detail.isdigit():
        idx = int(detail) - 1
        if 0 <= idx < len(notes):
            note = notes[idx]
            print(f"\nTitle: {note.title}")
            print(f"Timestamp: {format_timestamp(note.timestamp)}")
            print(f"Content:\n{note.content}\n")
        else:
            print("Invalid note number.")

def delete_note(notes):
    print("\n--- Delete Note ---")
    if not notes:
        print("No notes to delete.")
        return
    for idx, note in enumerate(notes, start=1):
        print(f"{idx}. [{format_timestamp(note.timestamp)}] {note.title}")
    to_del = input("Enter note number to delete (or press Enter to cancel): ").strip()
    if not to_del:
        print("Deletion cancelled.")
        return
    if to_del.isdigit():
        idx = int(to_del) - 1
        if 0 <= idx < len(notes):
            note = notes[idx]
            if get_confirmation(f"Are you sure you want to delete note '{note.title}'?"):
                notes.pop(idx)
                save_notes(NOTES_FILE, notes)
                print("Note deleted.")
            else:
                print("Deletion cancelled.")
        else:
            print("Invalid note number.")
    else:
        print("Invalid input.")

def main():
    try:
        notes = load_notes(NOTES_FILE)
    except Exception as e:
        print(f"Failed to load notes: {e}")
        notes = []

    while True:
        display_menu()
        choice = prompt_choice()
        if choice == '1':
            add_note(notes)
        elif choice == '2':
            view_notes(notes)
        elif choice == '3':
            delete_note(notes)
        elif choice == '4':
            print("Exiting.")
            save_notes(NOTES_FILE, notes)
            sys.exit(0)

if __name__ == "__main__":
    main()
