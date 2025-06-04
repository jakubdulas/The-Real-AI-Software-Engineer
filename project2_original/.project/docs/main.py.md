# main.py

## Overview
`main.py` provides the command-line interface (CLI) for the note manager application. It manages the interactive menu, user input, and delegates note creation, viewing, and deletion to supporting modules. This module acts as the orchestrator, ensuring a clean separation between the user interface and the underlying logic/data storage.

---

## Main Functions and Flow

### display_menu()
Prints the main menu with options to add, view, delete notes, or exit.

### prompt_choice()
Prompts the user to select a menu option (numbers 1-4), performing input validation and returning the validated choice as a string.

### add_note(notes)
Handles the process of adding a new note:
- Prompts the user for a title and content using input validation.
- Instantiates a new `Note`.
- Appends the note to the notes list and saves the updated list via `save_notes`.

### view_notes(notes)
Displays all notes in a numbered list with timestamps and titles.
- Allows the user to input a note number to view its details.

### delete_note(notes)
Handles note deletion:
- Displays the list of notes with numbers.
- Prompts for a note number to delete; confirms the deletion with the user.
- Removes the note and updates storage if confirmed.

### main()
The entry point:
- Loads notes from storage (using `load_notes` from `storage.py`).
- Enters the main loop, displaying the menu and handling user-selected actions.
- Saves all changes before exiting.

---

## Design and Implementation Details
- Imports the following modules:
  - `note` for the `Note` class
  - `storage` for note persistence
  - `utils` for input validation, confirmation, and timestamp formatting
- Persistent file is hardcoded as `notes.json` in the current directory.
- Ensures robust input validation and error handling for all actions.
- User-friendly prompts and clear feedback on all actions.

---

## Example usage
```bash
python main.py
```

---

## Dependencies
- `note.py` — Data model for notes
- `storage.py` — Functions for loading and saving notes
- `utils.py` — Input and formatting helpers
- Standard: `sys`

---

This module acts as the primary interface for users, delegating logic and persistence to external modules for a modular and maintainable design.