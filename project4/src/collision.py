"""
Module: collision.py
Collision detection logic for the Snake game.
"""

def snake_self_collision(snake_body):
    """Returns True if the head collides with the body."""
    return snake_body[0] in snake_body[1:]

def snake_wall_collision(snake_head, grid_size):
    """Returns True if the snake head is out of grid bounds."""
    x, y = snake_head
    return not (0 <= x < grid_size and 0 <= y < grid_size)

def snake_food_collision(snake_head, food_pos):
    """Returns True if the snake head collides with food."""
    return snake_head == food_pos
