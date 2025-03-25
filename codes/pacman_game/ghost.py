import random

class Ghost:
    def __init__(self, name, x, y):
        self.x = x
        self.y = y
        self.speed = 1  # Initial speed of the ghost
        self.name = name  # Name to identify the ghost

    def move_towards(self, target_x, target_y, grid):
        if self.x < target_x:
            new_x = self.x + self.speed
        elif self.x > target_x:
            new_x = self.x - self.speed
        else:
            new_x = self.x

        if self.y < target_y:
            new_y = self.y + self.speed
        elif self.y > target_y:
            new_y = self.y - self.speed
        else:
            new_y = self.y

        # Check for walls before moving
        if not grid.is_wall(new_x, new_y):
            self.x = new_x
            self.y = new_y

    def random_move(self, grid):
        direction = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        new_x = self.x + direction[0]
        new_y = self.y + direction[1]
        if not grid.is_wall(new_x, new_y):
            self.x = new_x
            self.y = new_y

    def get_position(self):
        return self.x, self.y
