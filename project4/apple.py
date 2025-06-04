import random

def get_random_apple_position(grid_width, grid_height, snake_body):
    """
    Utility function to return a random (x, y) position not overlapping the snake's body.
    """
    available = [
        (x, y) for x in range(grid_width)
        for y in range(grid_height)
        if (x, y) not in snake_body
    ]
    if not available:
        return None
    return random.choice(available)

class Apple:
    def __init__(self, grid_width, grid_height, snake_body):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.position = get_random_apple_position(grid_width, grid_height, snake_body)

    def respawn(self, snake_body):
        self.position = get_random_apple_position(self.grid_width, self.grid_height, snake_body)
