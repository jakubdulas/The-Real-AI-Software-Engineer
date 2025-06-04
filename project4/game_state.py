from snake import Snake
from apple import Apple

class GameState:
    def __init__(self, grid_width, grid_height, initial_snake_pos, move_delay):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.initial_snake_pos = initial_snake_pos
        self.move_delay = move_delay
        self.reset()

    def reset(self):
        self.snake = Snake(self.initial_snake_pos, 'RIGHT')
        self.apple = Apple(self.grid_width, self.grid_height, self.snake.get_body())
        self.score = 0
        self.last_move_time = 0
        self.game_over = False
