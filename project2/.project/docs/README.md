# Command-line Note Manager

A simple, modular Python application that allows you to create, view, and delete notes from the command line. Notes are stored persistently in a JSON file, with each note containing a title, content, and timestamp.

---

## Features
- **Create notes:** Add new notes with a title and content; timestamp added automatically.
- **View notes:** List all notes and view individual note details.
- **Delete notes:** Remove unwanted notes by title.
- **Persistent storage:** Notes are stored in a JSON file for longevity between sessions.
- **Terminal menu interface:** User-friendly navigation from the command line.

---

## Setup Instructions

1. **Clone the repository or download the source files.**
2. **(Optional but recommended)**: Use a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install requirements:**
   - No third-party requirements; uses Python standard library. Ensure Python 3.7+ is installed.
4. **Run the application:**
   ```bash
   python main.py
   ```

---

## Usage Instructions

1. **Launch the application:** Run `python main.py` in your terminal.
2. **Interactive menu:**
    - **Create a note:** Enter title and content when prompted.
    - **View notes:** List all notes, then select a note by its number to see details.
    - **Delete a note:** Enter the note's title to remove it.
    - **Exit:** Quit the application safely.

---

## Project Structure

```
.
├── main.py         # User interface and menu logic
├── note.py         # Note class (data model)
├── storage.py      # Functions to save/load notes from file
├── utils.py        # Helper functions (input validation, etc.)
├── notes.json      # (Auto-created) Persistent notes storage
└── README.md       # This documentation
```

---

## Additional Notes

- The first time you use the application, a `notes.json` file will be created in the same directory if it does not exist.
- All data is stored locally; there is no server-side storage.
- If you encounter issues or errors, ensure you have permission to write files in the application directory.

---

## License

This project is provided under the MIT License.
