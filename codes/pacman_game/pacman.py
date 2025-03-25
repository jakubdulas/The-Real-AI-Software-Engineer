class Pacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy, grid):
        new_x = self.x + dx
        new_y = self.y + dy
        if not grid.is_wall(new_x, new_y):
            self.x = new_x
            self.y = new_y

    def get_position(self):
        return self.x, self.y
