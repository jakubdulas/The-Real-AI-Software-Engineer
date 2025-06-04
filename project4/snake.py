"""
snake.py
Core Snake class representing the snake's body, direction, and movement logic.
"""

from collections import deque

# Directions as (dx, dy) tuples
direction_vectors = {
    'UP': (0, -1),
    'DOWN': (0, 1),
    'LEFT': (-1, 0),
    'RIGHT': (1, 0)
}

opposite_direction = {
    'UP': 'DOWN',
    'DOWN': 'UP',
    'LEFT': 'RIGHT',
    'RIGHT': 'LEFT'
}

class Snake:
    def __init__(self, initial_pos, initial_direction):
        self.body = deque([initial_pos])  # Each element is (x, y)
        self.direction = initial_direction  # String: 'UP', 'DOWN', ...
        self.next_direction = initial_direction
        self.grow_pending = False

    def set_direction(self, new_direction):
        """
        Set the snake's direction if not directly opposite.
        """
        if new_direction == opposite_direction[self.direction]:
            return  # Ignore reverse
        self.next_direction = new_direction

    def move(self):
        """
        Move the snake in the current direction.
        """
        self.direction = self.next_direction
        dx, dy = direction_vectors[self.direction]
        head_x, head_y = self.body[0]
        new_head = (head_x + dx, head_y + dy)
        self.body.appendleft(new_head)
        if self.grow_pending:
            self.grow_pending = False
        else:
            self.body.pop()

    def grow(self):
        self.grow_pending = True

    def get_head(self):
        return self.body[0]

    def get_body(self):
        return list(self.body)

    def check_collision(self, pos):
        """Return True if snake collides with given pos (excluding head)."""
        return pos in list(self.body)[1:]
