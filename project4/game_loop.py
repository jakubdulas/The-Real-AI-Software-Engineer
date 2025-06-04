import pygame
from snake import Snake
from apple import Apple
from renderer import Renderer

class GameLoop:
    def __init__(self, config):
        self.cell_size = config['cell_size']
        self.grid_width = config['grid_width']
        self.grid_height = config['grid_height']
        self.window_width = config['window_width']
        self.window_height = config['window_height']
        self.bg_color = config['bg_color']
        self.grid_color = config['grid_color']
        self.move_delay = config['move_delay']

        self.renderer = Renderer(self.cell_size, self.grid_width, self.grid_height,
                                 self.window_width, self.window_height, self.bg_color, self.grid_color)
        self.screen = None
        self.font = None
        self.clock = None

    def check_wall_collision(self, snake_head):
        x, y = snake_head
        return x < 0 or x >= self.grid_width or y < 0 or y >= self.grid_height

    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 32)
        
        initial_pos = (self.grid_width // 2, self.grid_height // 2)
        snake = Snake(initial_pos, 'RIGHT')
        score = 0
        apple = Apple(self.grid_width, self.grid_height, snake.get_body())
        last_move_time = pygame.time.get_ticks()

        direction_map = {
            pygame.K_UP: 'UP',
            pygame.K_DOWN: 'DOWN',
            pygame.K_LEFT: 'LEFT',
            pygame.K_RIGHT: 'RIGHT'
        }
        
        running = True
        game_over = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key in direction_map and not game_over:
                        snake.set_direction(direction_map[event.key])
                    if event.key == pygame.K_r and game_over:
                        # Restart the game
                        snake = Snake(initial_pos, 'RIGHT')
                        score = 0
                        apple = Apple(self.grid_width, self.grid_height, snake.get_body())
                        game_over = False
            if not game_over:
                current_time = pygame.time.get_ticks()
                if current_time - last_move_time > self.move_delay:
                    snake.move()
                    last_move_time = current_time
                    if snake.get_head() == apple.position:
                        snake.grow()
                        score += 1
                        apple.respawn(snake.get_body())
                    if self.check_wall_collision(snake.get_head()):
                        game_over = True
                    elif snake.check_collision(snake.get_head()):
                        game_over = True
            self.screen.fill(self.bg_color)
            self.renderer.draw_grid(self.screen)
            self.renderer.draw_snake(self.screen, snake)
            self.renderer.draw_apple(self.screen, apple.position)
            self.renderer.draw_score(self.screen, self.font, score)
            if game_over:
                self.renderer.draw_game_over(self.screen, self.font, self.window_width, self.window_height)
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()
