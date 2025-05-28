import sys
import pygame
from game import Game
from renderer import Renderer

# Constants
grid_size = 20  # Number of cells per row/column
grid_cell_size = 24  # Pixel size of each grid cell
window_size = grid_size * grid_cell_size


def main():
    pygame.init()
    screen = pygame.display.set_mode((window_size, window_size))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()
    renderer = Renderer(screen, grid_cell_size, grid_size, grid_size)
    
    def reset_game():
        return Game(grid_size)

    game = reset_game()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if game.game_over:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_r:
                        game = reset_game()
                else:
                    if event.key == pygame.K_UP:
                        game.snake.set_direction((0, -1))
                    elif event.key == pygame.K_DOWN:
                        game.snake.set_direction((0, 1))
                    elif event.key == pygame.K_LEFT:
                        game.snake.set_direction((-1, 0))
                    elif event.key == pygame.K_RIGHT:
                        game.snake.set_direction((1, 0))

        if not game.game_over:
            game.update()
        
        renderer.render(game)
        pygame.display.flip()
        clock.tick(10)  # 10 frames/sec (snake speed)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
