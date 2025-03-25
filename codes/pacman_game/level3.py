from grid import Grid
from pellet import Pellet
from pacman import Pacman
from ghost import Ghost

class Level3:
    def __init__(self):
        self.grid = Grid(30, 20)
        self.setup_level()

    def setup_level(self):
        # Create a maze-like structure and increase difficulty with more walls and less pellets...
        self.pellets = [Pellet(1, 1), Pellet(10, 18), Pellet(20, 5)]

    def get_grid(self):
        return self.grid
    
    def get_pellets(self):
        return self.pellets
