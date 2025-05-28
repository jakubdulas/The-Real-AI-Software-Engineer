# Snake Game

Welcome to the classic Snake game implemented in Python using Pygame! Guide your snake to eat apples, grow as long as possible, and avoid collisions with the walls or your own body.

## Table of Contents
- [Installation](#installation)
- [Running the Game](#running-the-game)
- [Gameplay Instructions](#gameplay-instructions)
- [Game Controls](#game-controls)
- [Objective](#objective)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Installation

1. **Clone the repository** (or download the source files):
   ```bash
   git clone <REPO_URL>
   cd <PROJECT_DIRECTORY>
   ```
2. **Set up a virtual environment** *(optional, but recommended)*:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   The only dependency is [Pygame](https://www.pygame.org/).

---

## Running the Game

Run the main game script using Python:

```bash
python main.py
```

---

## Gameplay Instructions
- The game starts with a short snake on a visible grid with an apple randomly placed on the screen.
- Use the keyboard arrow keys to control the snake's movement (UP, DOWN, LEFT, RIGHT).
- Guide the snake to eat apples. Each time the snake eats an apple, it grows longer and your score increases.
- The game ends if the snake runs into the walls or itself.
- The current score is displayed at the top of the window.

---

## Game Controls
- **Arrow Keys**: Move the snake (Up/Down/Left/Right)
- **ESC or Close Window**: Exit the game

---

## Objective
Grow your snake as long as you can by eating apples! Avoid crashing into the walls or your own tail.

Try to set a new high score!

---

## Troubleshooting
- **Pygame not found**: Ensure you have installed dependencies via `pip install -r requirements.txt`.
- **Game window doesn't appear**: Check that you are running the correct Python version (>=3.7) and that your display supports opening Pygame windows.

---

## License

This project is for educational and personal use. Modify and redistribute as you like!
