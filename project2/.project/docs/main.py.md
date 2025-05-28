# main.py Documentation

## Overview

`main.py` is the entry point for the command-line Note Manager application. It provides a simple terminal-based menu allowing users to create, view, and delete notes. This module interacts with the core logic and data storage modules to facilitate operation without exposing internal implementation details to the user.

## Module Responsibilities
- Display the main (and sub-) menu to the user.
- Gather and validate user input.
- Call logic functions from supporting modules to handle notes.
- Format and display output to the terminal.

## Menu Structure
Upon running the program, users interact with a looping, numbered menu:

```
=== Note Manager ===
1. Create note
2. List/View notes
3. Delete note
4. Exit
Select an option (1-4):
```

- **Create note**: Prompts for a note title and content, then saves.
- **List/View notes**: Lists existing notes, lets user view details by selecting a number.
- **Delete note**: Lists notes, lets user choose one to delete (with confirmation prompt).
- **Exit**: Closes the application.

## Usage Instructions

### Launching the Application
To start the note manager, from your terminal run:

```bash
python main.py
```

### Creating a Note
1. Select option `1` from the main menu.
2. Input a title (required, must not be empty).
3. Input the content (optional, can be empty).
4. On error (e.g. duplicate or blank title), an error message displays.

### Listing & Viewing Notes
1. Select option `2`.
2. A numbered list of notes (with titles and timestamps) appears.
3. Enter the note number to view its details, or press Enter to cancel.
4. If an invalid number is entered, you are prompted again.
5. Details displayed include title, content, and timestamp.

### Deleting a Note
1. Select option `3`.
2. Notes are listed; select a note's number to delete, or press Enter to cancel.
3. A confirmation prompt appears; type `y` to confirm, any other key to cancel.
4. Success/failure feedback is displayed.

## Input Validation
- Menu options must be integers 1–4; invalid entries prompt user to retry.
- Note indexes are 1-based; invalid selections (out of range, not a number) are handled gracefully.
- Delete/view operations can be cancelled by pressing Enter.

## Internal Flow and Module Collaboration
- **Menu/UI functions** in `main.py` (`create_note_ui()`, `list_and_view_notes_ui()`, `delete_note_ui()`) handle all user interaction and output.
- **Core Note Logic** is delegated to `note_manager` and `delete_note` modules, which perform note creation, retrieval, and deletion. Return values are checked for success/errors.
- **Format Helpers**: `format_timestamp` from `utils.py` is called to display timestamps in a user-friendly format.
- Validation and error handling are present throughout to ensure a robust CLI experience.

## Main Functions
- `main_menu()`: Primary event loop, presents the main menu and dispatches selected actions.
- `main()`: Entrypoint, calls the menu loop.
- Each UI function is responsible for interacting with the user and calling the appropriate backend logic.

----

*For further details on how notes are structured, saved, or manipulated, refer to the documentation for `note.py`, `storage.py`, and `utils.py`.*
