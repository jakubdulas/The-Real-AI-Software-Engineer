# snake.py Documentation

## Overview

Defines the `Snake` class: the main player character in the game. Maintains an ordered list of body segments, controls movement, direction, growth, and self-collision.

## Structure
- Uses `collections.deque` for fast appends/pops to represent the snake's body as a list of `(x, y)` tuples.
- Contains mapping for movement direction and rules for preventing direct reversal.

## Direction Mapping
- `direction_vectors`: Maps direction names (`'UP'`, `'DOWN'`, etc.) to (dx, dy) vectors.
- `opposite_direction`: Prevents invalid direction reversals (e.g., no going from 'UP' to 'DOWN' in one move).

## Snake Class

### `__init__(self, initial_pos, initial_direction)`
- Creates a new snake with a single head segment (`initial_pos`) and direction string.
- `.body` contains all segments (deque, each `[x, y]`).
- `.direction` is the current direction. `.next_direction` is updated via input.
- `.grow_pending` flags whether the snake should grow after next move.

### `set_direction(self, new_direction)`
- Changes the planned direction to `new_direction` only if not the opposite of current direction (prevents instant self-collision by reversing directly).

### `move(self)`
- Updates the snake's direction to the planned `next_direction`.
- Moves head in the new direction by adding a new head segment in front.
- Removes last tail segment (unless growth is pending).

### `grow(self)`
- Sets `grow_pending`, causing the next move to skip tail removal—lengthening the snake by 1.

### `get_head(self)`
- Returns `(x, y)` of the snake's current head (front segment).

### `get_body(self)`
- Returns a list of all snake segments (for collision/meal placement).

### `check_collision(self, pos)`
- Returns `True` if the given position `pos` is in the snake body (excluding head).
- Used to check self-collision after moving.

## Extending and Modifying
- To change the snake's initial length, in `__init__()` add more segments to `self.body`.
- To implement additional mechanics (e.g., shrinking, invulnerability, etc.), add logic to `move()` or new methods.
