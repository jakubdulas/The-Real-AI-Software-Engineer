import pygame

class Renderer:
    def __init__(self, cell_size, grid_width, grid_height, window_width, window_height, bg_color, grid_color):
        self.cell_size = cell_size
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.window_width = window_width
        self.window_height = window_height
        self.bg_color = bg_color
        self.grid_color = grid_color

    def draw_grid(self, surface):
        for x in range(0, self.window_width, self.cell_size):
            pygame.draw.line(surface, self.grid_color, (x, 0), (x, self.window_height))
        for y in range(0, self.window_height, self.cell_size):
            pygame.draw.line(surface, self.grid_color, (0, y), (self.window_width, y))

    def draw_snake(self, surface, snake):
        for x, y in snake.get_body():
            rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
            pygame.draw.rect(surface, (0, 255, 0), rect)

    def draw_apple(self, surface, pos):
        rect = pygame.Rect(pos[0] * self.cell_size, pos[1] * self.cell_size, self.cell_size, self.cell_size)
        pygame.draw.rect(surface, (255, 0, 0), rect)

    def draw_score(self, surface, font, score):
        score_surface = font.render(f"Score: {score}", True, (255, 255, 255))
        surface.blit(score_surface, (10, 8))

    def draw_game_over(self, surface, font, window_width, window_height):
        go_text = font.render("GAME OVER! Press R to restart", True, (255, 64, 64))
        surface.blit(go_text, (window_width // 2 - go_text.get_width() // 2, window_height // 2 - 20))
