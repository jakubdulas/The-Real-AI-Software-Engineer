# game_loop.py Documentation

## Overview

This file defines the main game controller via the `GameLoop` class. It coordinates user input, timing, main Snake and Apple logic, collision handling, rendering, and game state management (including scoring and restart).

## Major Components
- Imports:
    - `pygame` for windowing, graphics, events, and timing.
    - `Snake` (from `snake.py`): Main snake movement and logic.
    - `Apple` (from `apple.py`): Manages random food spawning.
    - `Renderer` (from `renderer.py`): All graphical rendering.

## The `GameLoop` Class

### Initialization (`__init__`)
- Takes configuration dictionary (cell/grid/window size, colors, speed, etc.).
- Prepares the renderer.
- No Pygame window or clock is started here; this is done in `run()`.

### `check_wall_collision(snake_head)`
- Returns `True` if `snake_head` (tuple) is outside grid boundaries, else `False`.

### `run()`
- Initializes Pygame and the main window, font, and clock.
- Places the snake in the center facing right; creates the first apple, initializes score.
- Keeps track of the snake's direction, manages the main event loop:
    - Processes events (QUIT, arrow keys for direction, 'R' for restart on Game Over).
    - Handles timing so snake moves at fixed time intervals.
    - Updates the snake's position, checks for apple consumption, and grows/respawns apple as needed.
    - Game ends on wall collision or when snake hits itself (self-collision logic).
    - Delegates all drawing to the Renderer (snake, apple, grid, score, and game-over text).
    - Manages frame rate and handles clean pygame shutdown.

#### Event Handling / Input
- Arrow keys change direction, but cannot directly reverse.
- 'R' key restarts the game *after* game over.
- Window close exits the game.

#### Collision Logic
- Uses `check_wall_collision()` for wall checks.
- Calls `snake.check_collision()` to see if the head hits its body.

#### Rendering
- Draws background, grid, snake, apple, score, and game over screen via Renderer.

#### Extending/Modifying
- Adjust `move_delay` for snake speed.
- Change scoring or apple mechanics by modifying apple logic.
- Add more features (e.g., obstacles) by inserting logic before/after snake movement.
- For UI overlays/fancier graphics, extend the Renderer class.

---

## Game Loop Responsibilities
- **Game loop orchestration**: Handles all main game states and frame updates.
- **Input handing**: Delegates valid inputs, ignoring reverse direction changes.
- **Collision and death**: Cleanly halts the game, allowing restart or quit.
- **Drawing**: Uses a dedicated Renderer for all visuals.