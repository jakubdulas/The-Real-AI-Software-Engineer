class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[0 for _ in range(width)] for _ in range(height)]
        self.walls = []

    def add_wall(self, x, y):
        self.cells[y][x] = 1
        self.walls.append((x, y))

    def is_wall(self, x, y):
        return self.cells[y][x] == 1

    def get_size(self):
        return self.width, self.height
