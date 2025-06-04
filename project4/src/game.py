import random
from . import collision

class SnakeGame:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.reset()

    def reset(self):
        self.snake = [(self.grid_size // 2, self.grid_size // 2)]
        self.direction = (0, -1)
        self.apple = self.random_apple_position()
        self.score = 0
        self.grow_snake = False
        self.alive = True

    def random_apple_position(self):
        available = [
            (x, y)
            for x in range(self.grid_size)
            for y in range(self.grid_size)
            if (x, y) not in self.snake
        ]
        return random.choice(available)

    def update_direction(self, new_direction):
        # Prevent reverse
        if (
            (new_direction[0] == -self.direction[0] and new_direction[1] == -self.direction[1])
            or (new_direction == self.direction)
        ):
            return
        self.direction = new_direction

    def update(self):
        if not self.alive:
            return
        head = (
            self.snake[0][0] + self.direction[0],
            self.snake[0][1] + self.direction[1],
        )
        # Check collisions
        if collision.check_wall_collision(head, self.grid_size, self.grid_size) or \
           collision.check_self_collision([head] + self.snake):
            self.alive = False
            return
        self.snake.insert(0, head)
        if head == self.apple:
            self.score += 1
            self.apple = self.random_apple_position()
            # grow snake: do not pop tail
        else:
            self.snake.pop()

    def get_snake(self):
        return self.snake

    def get_apple(self):
        return self.apple

    def get_score(self):
        return self.score

    def is_alive(self):
        return self.alive
