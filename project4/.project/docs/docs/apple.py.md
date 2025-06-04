# apple.py Documentation

## Overview

Defines the logic for food (Apple) placement in the Snake game. Handles spawning and respawning the apple on the grid, avoiding overlap with the snake.

## Major Components

### Utility Function: `get_random_apple_position(grid_width, grid_height, snake_body)`
- Picks a random, unoccupied cell from the grid for the apple.
- Excludes any slot currently occupied by the snake.
- Returns `(x, y)` grid tuple or `None` if no open cell (extremely rare—only if snake fills the grid!).

### Class: `Apple`
- **Initialization:**
    - Requires grid size (`grid_width`, `grid_height`) and the current snake body to avoid collisions.
    - Sets `self.position` to a new random free cell.
- **Method:** `respawn(snake_body)`
    - When eaten, call this to move apple to another unoccupied cell (providing updated snake body list).
    - Updates `self.position` accordingly.

## Extending/Modifying
- To add special apples or powerups: subclass or add properties to Apple.
- For more complicated spawning (e.g., farther from snake, or based on level): Adjust logic within `get_random_apple_position()` or `respawn()` accordingly.
