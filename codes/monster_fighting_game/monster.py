import pygame


class Monster:
    def __init__(self, x, y, health):
        self.x = x  # x position on the grid
        self.y = y  # y position on the grid
        self.health = health  # Monster health
        self.size = 20  # Size of the monster square

    def draw(self, screen):
        pygame.draw.rect(
            screen, (255, 0, 0), (self.x, self.y, self.size, self.size)
        )  # Draw monster as a red square

    def move_towards(self, target_pos):
        if self.x < target_pos[0]:
            self.x += 1
        elif self.x > target_pos[0]:
            self.x -= 1
        if self.y < target_pos[1]:
            self.y += 1
        elif self.y > target_pos[1]:
            self.y -= 1

    def attack(self):
        # Placeholder for attack logic (if needed in the future)
        pass
