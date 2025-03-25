from grid import Grid
from pellet import Pellet
from pacman import Pacman
from ghost import Ghost

class Level2:
    def __init__(self):
        self.grid = Grid(30, 20)
        self.setup_level()

    def setup_level(self):
        # Setup walls and more complex structures than Level 1...
        self.pellets = [Pellet(5, 5), Pellet(10, 10), Pellet(15, 15)]  # Example

    def get_grid(self):
        return self.grid
    
    def get_pellets(self):
        return self.pellets
