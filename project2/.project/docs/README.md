# Command-Line Note Manager

A modular Python application for taking notes from the command line. Each note includes a title, content, and timestamp. Notes are stored persistently in a JSON file.

## Features
- Add, view, and delete notes from an interactive terminal menu.
- Each note includes a title, content, and creation timestamp.
- Persistent JSON storage.
- Modular codebase for easy maintenance and extension.

## Project Structure
```
.
├── main.py         # Command-line interface and menu logic
├── note.py         # Note data class
├── storage.py      # Functions for saving/loading notes
├── utils.py        # General helper functions
└── README.md       # This documentation file
```

## Setup
1. **Python version:** Requires Python 3.7 or newer.
2. **Clone/download the repository** to your computer.
3. **No third-party dependencies** – uses only the standard library.

## Usage
1. Open a terminal in this project directory.
2. Run the application:
    ```
    python main.py
    ```
3. Follow the on-screen prompts:
    - **Add Note**: Enter a title and content. A timestamp will be added automatically.
    - **View Notes**: Shows notes with timestamps; enter a number to view full details.
    - **Delete Note**: Select the note number to delete; confirmation is required.
    - **Exit**: Saves all notes and exits.

## Data Storage
- Notes are stored in a `notes.json` file in the same directory.
- If the file doesn't exist, it will be created automatically.

## Module Documentation
See the following files for detailed reference:
- [main.py.md](./main.py.md)
- [note.py.md](./note.py.md)
- [storage.py.md](./storage.py.md)
- [utils.py.md](./utils.py.md)

## Safety & Tips
- All input is validated for correctness and completeness.
- If `notes.json` is corrupted or deleted, the program will start with an empty note list.
- Edits are saved automatically after add/delete.

---

**Enjoy managing your notes securely and efficiently from the terminal!**
