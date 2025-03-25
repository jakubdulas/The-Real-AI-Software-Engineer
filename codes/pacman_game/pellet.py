class Pellet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.collected = False

    def collect(self):
        self.collected = True
