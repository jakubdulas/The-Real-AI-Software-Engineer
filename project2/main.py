import sys
from utils import validate_menu_choice, validate_note_title, validate_note_content
from storage import NoteStorage
from note import Note


def main_menu():
    """
    Display the main menu and handle navigation.
    """
    storage = NoteStorage()

    while True:
        notes = storage.list_notes()
        print("\n------ Note Manager ------")
        print("Notes:")
        if not notes:
            print("  (No notes found)")
        else:
            for idx, note in enumerate(notes):
                print(f"  {idx + 1}. {note.title} ({note.timestamp})")
        print("\nMenu:")
        print("  1. Create new note")
        print("  2. View note details")
        print("  3. Delete note")
        print("  4. Exit")

        choice = input("Choose an option (1-4): ").strip()
        if not validate_menu_choice(choice, ["1", "2", "3", "4"]):
            print("Invalid option. Please try again.")
            continue

        if choice == "1":
            # Create new note
            title = input("Enter note title: ").strip()
            while not validate_note_title(title):
                print("Title cannot be empty or exceed 100 characters.")
                title = input("Enter note title: ").strip()
            content = input("Enter note content: ").strip()
            while not validate_note_content(content):
                print("Content cannot be empty or exceed 2000 characters.")
                content = input("Enter note content: ").strip()
            note = Note(title, content)
            storage.add_note(note)
            print("Note added successfully!")

        elif choice == "2":
            # View note details
            if not notes:
                print("No notes available.")
                continue
            idx = input(f"Enter the note number to view (1-{len(notes)}): ").strip()
            if not (idx.isdigit() and 1 <= int(idx) <= len(notes)):
                print("Invalid note selection.")
                continue
            note = notes[int(idx) - 1]
            print("\n------ Note Details ------")
            print(f"Title: {note.title}")
            print(f"Timestamp: {note.timestamp}")
            print(f"Content:\n{note.content}")
            print("--------------------------")

        elif choice == "3":
            # Delete note
            if not notes:
                print("No notes to delete.")
                continue
            idx = input(f"Enter the note number to delete (1-{len(notes)}): ").strip()
            if not (idx.isdigit() and 1 <= int(idx) <= len(notes)):
                print("Invalid note selection.")
                continue
            confirm = (
                input(
                    f"Are you sure you want to delete '{notes[int(idx)-1].title}'? (y/N): "
                )
                .strip()
                .lower()
            )
            if confirm == "y":
                storage.delete_note(int(idx) - 1)
                print("Note deleted.")
            else:
                print("Deletion cancelled.")

        elif choice == "4":
            print("Goodbye!")
            sys.exit()


if __name__ == "__main__":
    main_menu()
