"""
main.py
--------
Command-line interface and main menu for Note Manager.
"""

from note_manager import create_note_logic, get_notes_summaries, get_note_detail
from delete_note import delete_note_logic
from utils import format_timestamp


def format_timestamp_string(timestamp_iso: str) -> str:
    from datetime import datetime

    try:
        dt = datetime.fromisoformat(timestamp_iso)
        return format_timestamp(dt)
    except Exception:
        return timestamp_iso


def create_note_ui():
    print("\n-- Create a New Note --")
    title = input("Title: ").strip()
    content = input("Content: ").strip()
    err = create_note_logic(title, content)
    if err:
        print(f"Error: {err}")
        return
    print(f"Note '{title}' created successfully.")


def list_and_view_notes_ui():
    print("\n-- Your Notes --")
    summaries = get_notes_summaries()
    if not summaries:
        print("No notes found.")
        return
    for summary in summaries:
        print(
            f"{summary['index']}. {summary['title']} [{format_timestamp_string(summary['timestamp'])}]"
        )
    try:
        choice = input("Select note number to view details (Enter to cancel): ").strip()
        if not choice:
            return
        index = int(choice) - 1
        if index < 0 or index >= len(summaries):
            print("Invalid selection.")
            return
        note = get_note_detail(index)
        if note is None:
            print("Note not found.")
            return
        print("\n--- Note Details ---")
        print(f"Title     : {note.title}")
        print(f"Timestamp : {format_timestamp_string(note.timestamp)}")
        print(f"Content   :\n{note.content}\n")
    except ValueError:
        print("Invalid input. Please enter a valid note number.")


def delete_note_ui():
    print("\n-- Delete a Note --")
    summaries = get_notes_summaries()
    if not summaries:
        print("No notes available to delete.")
        return
    for summary in summaries:
        print(
            f"{summary['index']}. {summary['title']} [{format_timestamp_string(summary['timestamp'])}]"
        )
    try:
        choice = input("Select note number to delete (Enter to cancel): ").strip()
        if not choice:
            return
        index = int(choice) - 1
        if index < 0 or index >= len(summaries):
            print("Invalid selection.")
            return
        confirm = (
            input(
                f"Are you sure you want to delete note '{summaries[index]['title']}'? (y/N): "
            )
            .strip()
            .lower()
        )
        if confirm != "y":
            print("Deletion cancelled.")
            return
        err = delete_note_logic(index)
        if err:
            print(f"Error: {err}")
        else:
            print("Note deleted successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid note number.")


def main_menu():
    while True:
        print("\n=== Note Manager ===")
        print("1. Create note")
        print("2. List/View notes")
        print("3. Delete note")
        print("4. Exit")
        choice = input("Select an option (1-4): ").strip()
        if choice == "1":
            create_note_ui()
        elif choice == "2":
            list_and_view_notes_ui()
        elif choice == "3":
            delete_note_ui()
        elif choice == "4":
            print("Exiting Note Manager. Goodbye!")
            break
        else:
            print("Invalid selection. Please try again.")


def main():
    main_menu()


if __name__ == "__main__":
    main()
