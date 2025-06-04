# Tic Tac Toe (Terminal-Based)

## Overview
This is a modular, terminal-based Tic Tac Toe game written in Python. It supports:
- Two human players alternating turns
- Human vs. simple AI opponent
- Input validation (prevents overwriting cells)
- ASCII display of the board after each move
- Win/draw detection and game end messages

The code is structured to be easily extendable: main components are separated via classes and functions for Board, Player, Game Logic, and AI modules.

---

## How to Run the Game
1. **Install Python 3** if not already installed (https://python.org).
2. **Save the game code** to a file named `tictactoe.py` in your preferred directory.
3. **Open your terminal** and navigate to the directory containing `tictactoe.py`
4. **Run the game:**
   ```bash
   python tictactoe.py
   ```

---

## Game Features
- **Player Modes:**
  - Human vs Human
  - Human vs AI (Easy mode)
- **Input Validation:**
  - Accepts only valid (empty) board positions (1-9)
- **Display:**
  - Board state printed after each move using ASCII art
- **Game End Detection:**
  - Detects when a player wins or if the game ends in a draw
  
---

## Code Organization
- **Board**: Manages the game state and board display
- **Player**: Handles player identity and move logic
- **AI**: Contains simple AI logic for automated moves
- **Game**: Orchestrates turns, input, win/draw checking

Each class/function in the code includes detailed docstrings for easy extensibility.

---

## Extending the Game
See `docs/EXTENDING_THE_GAME.md` for developer guidance on adding advanced AI, GUIs, network features, and other improvements.
