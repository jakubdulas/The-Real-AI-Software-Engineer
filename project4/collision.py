class Collision:
    def __init__(self, grid_width, grid_height):
        self.grid_width = grid_width
        self.grid_height = grid_height

    def check_wall_collision(self, snake_head):
        x, y = snake_head
        return x < 0 or x >= self.grid_width or y < 0 or y >= self.grid_height

    def check_self_collision(self, snake):
        return snake.check_collision(snake.get_head())
