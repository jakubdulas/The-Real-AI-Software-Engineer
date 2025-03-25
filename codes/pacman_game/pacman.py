import pygame
from settings import GRID_SIZE

class PacMan:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = GRID_SIZE
        self.color = (255, 255, 0)  # Yellow

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))