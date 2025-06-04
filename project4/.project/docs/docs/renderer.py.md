# renderer.py Documentation

## Overview

Responsible for all graphical rendering in the Snake game. The `Renderer` class encapsulates drawing the grid, snake, apple, score display, and game over message.

## Renderer Class

### Initialization (`__init__`)
- Takes all spatial, color, and size configuration needed for rendering.
- Caches window, grid settings, cell size, and colors for use in all draw calls.

### `draw_grid(surface)`
- Draws vertical and horizontal lines to visually separate grid cells.
- Rendered on the provided Pygame `surface`.

### `draw_snake(surface, snake)`
- Fills each segment of the snake as a green (0,255,0) rectangle at the scaled position.
- Uses `snake.get_body()` to retrieve all body parts.

### `draw_apple(surface, pos)`
- Draws a single red (255,0,0) cell at the apple's `(x, y)` grid coordinate.

### `draw_score(surface, font, score)`
- Renders current score as white text on the top left.
- Uses provided Pygame `font` object for rendering.

### `draw_game_over(surface, font, window_width, window_height)`
- Displays a red "GAME OVER! Press R to restart" centered on screen.

## Extending and Modifying
- Change colors or add effects by editing color values in relevant `draw_` methods.
- Can add more visual states (flashing, animations, etc.) by inserting draws or new methods.
- To support more complex shapes or graphics, change from rectangles to Pygame sprites or images.
