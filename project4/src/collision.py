# collision.py

def check_wall_collision(snake_head, grid_width, grid_height):
    """Check if the snake's head collides with the wall."""
    x, y = snake_head
    return x < 0 or x >= grid_width or y < 0 or y >= grid_height


def check_self_collision(snake):
    """
    Check if the snake's head collides with its own body.
    snake: list of (x, y) positions. Head == snake[0]
    """
    head = snake[0]
    return head in snake[1:]
