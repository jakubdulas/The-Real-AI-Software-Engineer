import os
from note import Note
from storage import save_notes_to_file, load_notes_from_file
from utils import (
    is_empty_input,
    sanitize_string,
    format_timestamp,
    validate_menu_choice,
    validate_note_title,
    sanitize_text,
)


def main():
    FILENAME = "notes.json"
    notes = load_notes_from_file(FILENAME)

    while True:
        print("\n--- Command-Line Note Manager ---")
        print("1. Create a new note")
        print("2. View all notes")
        print("3. Delete a note")
        print("4. Exit")
                choice = input("Select an option (1-4): ").strip()
        if not validate_menu_choice(choice):
            print("Invalid choice. Please enter a number between 1 and 4.")
            continue

        if choice == "1":
            while True:
                title = input("Enter note title: ")
                if not validate_note_title(title):
                    print(
                        "Error: Title must be 1-100 characters and not just whitespace."
                    )
                else:
                    title = sanitize_text(title)
                    break
            while True:
                content = input("Enter note content: ")
                sanitized_content = sanitize_text(content)
                if is_empty_input(sanitized_content):
                    print("Error: Content cannot be empty. Please try again.")
                else:
                    content = sanitized_content
                    break
            new_note = Note(title, content)
            notes.append(new_note)
            save_notes_to_file(notes, FILENAME)
            print("Note added successfully.")

        elif choice == "2":
            if not notes:
                print("No notes saved.")
                continue
            print("\n--- Saved Notes ---")
            for idx, note in enumerate(notes, start=1):
                print(f"{idx}. {note.title}")
                print(f"   {format_timestamp(note.timestamp)}")
                print(f"   {note.content}")
                print("-------------------------")

        elif choice == "3":
            if not notes:
                print("No notes to delete.")
                continue
            print("\n--- Delete a Note ---")
            for idx, note in enumerate(notes, start=1):
                print(f"{idx}. {note.title} ({format_timestamp(note.timestamp)})")
            try:
                to_delete = int(input("Enter the note number to delete: "))
                if not (1 <= to_delete <= len(notes)):
                    print("Invalid note number.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            deleted_note = notes.pop(to_delete - 1)
            save_notes_to_file(notes, FILENAME)
            print(f"Note '{deleted_note.title}' deleted.")

        elif choice == "4":
            print("Exiting Note Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
