import sys
import pygame
from game import SnakeGame
import renderer
import input_handler

CELL_SIZE = renderer.CELL_SIZE
GRID_SIZE = 20
WINDOW_SIZE = CELL_SIZE * GRID_SIZE
FPS = 10

def main():
    pygame.init()
    window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("arial", 24)
    game = SnakeGame(GRID_SIZE)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            new_dir = input_handler.get_direction_from_event(event)
            if new_dir is not None:
                game.update_direction(new_dir)
        if game.is_alive():
            game.update()
        window.fill(renderer.BG_COLOR)
        renderer.draw_grid(window, GRID_SIZE)
        renderer.draw_snake(window, game.get_snake())
        renderer.draw_apple(window, game.get_apple())
        renderer.draw_score(window, game.get_score(), font)
        if not game.is_alive():
            gameover_text = font.render('Game Over! Press ESC to quit.', True, (255, 100, 100))
            window.blit(gameover_text, (30, WINDOW_SIZE // 2 - 18))
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                running = False
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
