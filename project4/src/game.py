from mechanics import Snake, Food
from collision import snake_self_collision, snake_wall_collision

class Game:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.snake = Snake((grid_size // 2, grid_size // 2))
        self.food = Food(grid_size, self.snake.body)
        self.score = 0
        self.game_over = False

    def update(self):
        if self.game_over:
            return
        self.snake.update()
        head = self.snake.body[0]
        # Collision with walls
        if snake_wall_collision(head, self.grid_size):
            self.game_over = True
            return
        # Collision with itself
        if snake_self_collision(self.snake.body):
            self.game_over = True
            return
        # Check if snake ate the apple
        if head == self.food.position:
            self.snake.queue_grow()
            self.food.respawn(self.snake.body)
            self.score += 1

    def draw(self, surface, cell_size):
        self.snake.draw(surface, cell_size)
        self.food.draw(surface, cell_size)
        # The score is now always accessible as self.score for rendering
