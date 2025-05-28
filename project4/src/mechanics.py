import pygame
import random

SNAKE_COLOR = (0, 200, 0)
FOOD_COLOR = (200, 30, 30)

class Snake:
    def __init__(self, initial_pos, initial_length=3):
        self.body = [
            (initial_pos[0] - i, initial_pos[1])
            for i in range(initial_length)
        ]
        self.direction = (1, 0)  # initial movement: right
        self.pending_direction = (1, 0)
        self.grow_pending = False

    def set_direction(self, dir_tuple):
        # Prevent reversing into itself
        if (dir_tuple[0] == -self.direction[0] and dir_tuple[1] == -self.direction[1]):
            return
        self.pending_direction = dir_tuple

    def update(self):
        # update direction for this frame
        self.direction = self.pending_direction
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        self.body.insert(0, new_head)

        if self.grow_pending:
            self.grow_pending = False
        else:
            self.body.pop()

    def queue_grow(self):
        self.grow_pending = True

    def check_self_collision(self):
        """Returns True if the snake's head collides with its body."""
        return self.body[0] in self.body[1:]

    def draw(self, surface, cell_size):
        for segment in self.body:
            rect = pygame.Rect(
                segment[0] * cell_size,
                segment[1] * cell_size,
                cell_size, cell_size
            )
            pygame.draw.rect(surface, SNAKE_COLOR, rect)

class Food:
    def __init__(self, grid_size, snake_body):
        self.grid_size = grid_size
        self.position = self.random_position(snake_body)

    def random_position(self, snake_body):
        available = [
            (x, y)
            for x in range(self.grid_size)
            for y in range(self.grid_size)
            if (x, y) not in snake_body
        ]
        return random.choice(available) if available else (0, 0)

    def respawn(self, snake_body):
        self.position = self.random_position(snake_body)

    def draw(self, surface, cell_size):
        rect = pygame.Rect(
            self.position[0] * cell_size,
            self.position[1] * cell_size,
            cell_size, cell_size
        )
        pygame.draw.rect(surface, FOOD_COLOR, rect)
