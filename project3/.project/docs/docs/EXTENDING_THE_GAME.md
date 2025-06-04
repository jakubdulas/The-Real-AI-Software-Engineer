# Extending the Game

This section provides guidance for developers who wish to extend or enhance the Tic Tac Toe game. The codebase is designed to be modular and easy to adapt. Here you'll find suggestions on adding new features, advice on where to modify the existing code, and a reference of key classes and functions to help you get started quickly.

## 1. Implementing More Advanced AI

- **File to modify:** `tic_tac_toe.py` (example; adapt to your filename/project structure)
- **Class to extend:** `AIPlayer` or the `ai_move` function.
- **Ideas:**
  - Implement minimax or another decision-making algorithm.
  - Create different AI difficulty levels by subclassing Player or AIPlayer.
- **Reference:**
  - `AIPlayer.make_move(board)`
  - `ai_move(board, ai_marker)`
  - AI logic currently resides in the AI player class or the `ai_move` function; simply swap out the logic or add new methods.

## 2. Adding a GUI

- **Suggestion:**
  - Integrate with GUI frameworks such as `tkinter`, `PyGame`, or `Kivy`.
  - Replace or supplement the ASCII `Board.display()` function with graphical output.
- **Reference:**
  - `Board.display()` – this is responsible for board output. Overriding or supplementing this method is a good starting point for GUI integration.
  - Input handling is currently via the terminal; refactor input logic into a separate handler to make connecting to button-clicks or mouse-events easier.

## 3. Enabling Network Play

- **Suggestion:**
  - Refactor the `Player` class so it can fetch moves from network sources.
  - Use Python libraries such as `socket`, `asyncio`, or third-party libraries to communicate moves.
- **Reference:**
  - `Player.get_move(board)` – by overriding this method, you can receive moves from a network peer.
  - Game loop in `Game.run()` – you may want to update this loop to coordinate turns over a network.

## 4. Supporting Larger or Custom Boards

- **Suggestions:**
  - Refactor `Board` class to accept variable size and win-length parameters.
  - Update win-checking logic in `Board.check_win()` to accommodate new board sizes and win conditions.
- **Reference:**
  - `Board.__init__(size=3, win_length=3)` – extend constructor to add flexibility.

## 5. Module and Function Reference for Extensibility

- **`Board` Class:**
  - `display()`: Outputs the board (can be overridden for different UIs).
  - `is_full()`, `is_empty_at(x, y)`, `place_marker(x, y, marker)`: Core state management.
  - `check_win(marker)`: Adjust for new win conditions or board sizes.
- **`Player` Classes:**
  - `get_move(board)`: Used by all player types (human, AI, network) to provide next move.
- **`Game` Class:**
  - `run()`: Main game loop; adapt this for new ways of sequencing turns or managing state.
- **`AI` Functions/Classes:**
  - `ai_move(board, marker)`: AI logic entry point for computer moves.

## Tips for Extending

- Keep new features encapsulated to allow easy toggling or modification.
- Use inheritance or composition when adding new player types (e.g., `NetworkPlayer`, `AdvancedAIPlayer`).
- If moving to a package structure, place classes in separate modules (`board.py`, `player.py`, etc.) for maintainability.
- Document new endpoints and logic in this guide for team consistency.

---
For further details on each function or class, read inline comments and the code documentation. Happy coding!