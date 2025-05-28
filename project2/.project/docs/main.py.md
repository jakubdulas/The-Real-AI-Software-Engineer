# `main.py`

## Overview

The `main.py` file provides the command-line interface (CLI) for the note manager application. It manages user interaction, displays menus, collects user input, and invokes storage and validation logic to perform note operations (create, read, delete).

---

## Module Responsibility
- Presents and handles the terminal menu system.
- Collects and validates user input for various actions.
- Acts as the entry-point for running the application.
- Delegates data storage/retrieval to `storage.py` and note representation to `note.py`.

---

## Main Logic Flow
- Start the app with `main_menu()` if run as the main program.
- Continuously show a menu:
    - List all notes with indices and timestamps
    - Offer options: Create note, View details, Delete note, Exit
- Use validator functions from `utils.py` to check input for menu choices and note data
- Use `NoteStorage` from `storage.py` for CRUD operations on notes (persisted in JSON file)
- Use `Note` objects to encapsulate note data

---

## Main Functions

### `main_menu()`
Implements the interactive menu loop. Steps include:
- Displays all current notes (with index and timestamps).
- Offers user menu with available actions.
- Handles note creation (with validation).
- Handles viewing full note details.
- Handles note deletion (with confirmation and validation).
- Loops until user chooses to exit (triggers `sys.exit()`).

#### Example Usage
```shell
$ python main.py
------ Note Manager ------
Notes:
  1. Shopping (2024-04-25T16:22:01)
...
Menu:
  1. Create new note
  2. View note details
  3. Delete note
  4. Exit
```

---

## Example Code Snippet
```python
from storage import NoteStorage
from note import Note
from utils import validate_note_title

storage = NoteStorage()
notes = storage.get_all_notes()
if validate_note_title("My Note"):
    note = Note("My Note", "Content")
    storage.add_note(note)
```

---

## Developer Notes
- All input/output is handled via standard input/output (terminal/console).
- Core business logic is kept in storage/note modules; `main.py` coordinates interaction.
- To extend functionality (e.g. search/filter), expand the menu loop.
