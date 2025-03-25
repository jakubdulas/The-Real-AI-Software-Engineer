import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from pacman import PacMan

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Pac-Man')
    clock = pygame.time.Clock()
    pacman = PacMan(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx = -pacman.size
        if keys[pygame.K_RIGHT]:
            dx = pacman.size
        if keys[pygame.K_UP]:
            dy = -pacman.size
        if keys[pygame.K_DOWN]:
            dy = pacman.size

        pacman.move(dx, dy)

        screen.fill((0, 0, 0))  # Clear the screen
        pacman.draw(screen)
        pygame.display.flip()  # Update the display
        clock.tick(FPS)  # Maintain the frame rate

if __name__ == '__main__':
    main()