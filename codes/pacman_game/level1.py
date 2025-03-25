from grid import Grid
from pellet import Pellet
from pacman import Pacman
from ghost import Ghost

class Level1:
    def __init__(self):
        self.grid = Grid(30, 20)
        self.setup_level()

    def setup_level(self):
        # Add walls
        for x in range(30):
            self.grid.add_wall(x, 0)  # Top
            self.grid.add_wall(x, 19)  # Bottom
        for y in range(20):
            self.grid.add_wall(0, y)  # Left
            self.grid.add_wall(29, y)  # Right

        # Add pellets
        self.pellets = [Pellet(x, y) for x in range(1, 29) for y in range(1, 19)]
        # More complex wall structures for level design...

    def get_grid(self):
        return self.grid
    
    def get_pellets(self):
        return self.pellets
