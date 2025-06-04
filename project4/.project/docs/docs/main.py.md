# main.py Documentation

## Overview

This is the entry point for the Snake game. It sets up game and window parameters, i.e., grid size, window size, colors, and game timing, and initializes the main game loop.

## Structure
- Imports `GameLoop` from `game_loop.py`.
- Defines configurations (grid, colors, cell size, etc.) in the `config` dictionary.
- Instantiates and runs the main game loop with these settings.

## Main Function

### `main()`
- **Purpose**: Configures essential constants and launches the `GameLoop`.
- **Grid/Window Constants**: 
    - `CELL_SIZE`: The pixel width/height of each grid cell.
    - `GRID_WIDTH`/`GRID_HEIGHT`: Grid dimensions (number of cells).
    - `WINDOW_WIDTH`/`WINDOW_HEIGHT`: Calculated from cell/grid sizes for display.
    - `BG_COLOR`, `GRID_COLOR`: RGB tuples for background/grid line colors.
    - `MOVE_DELAY`: Milliseconds between snake moves (controls speed).
- **Flow**:
    - All configuration constants are collected into a `config` dict for modularity.
    - The `GameLoop` class is instantiated with `config`.
    - `game.run()` launches the main game loop and renders the window.

## How to Extend or Modify
- Change `CELL_SIZE`, `GRID_WIDTH`, `GRID_HEIGHT` for different play areas.
- Adjust `MOVE_DELAY` to make the snake move faster/slower.
- Modify colors in `BG_COLOR` and `GRID_COLOR` for custom themes.
- To swap starting direction, adjust the `initial_direction` (via `GameLoop`).

## Example Usage
This file is intended to be run directly:
```bash
python main.py
```
It will open the game window and run the Snake game.