import pygame

CELL_SIZE = 24
GRID_COLOR = (40, 40, 40)
BG_COLOR = (0, 0, 0)
SNAKE_COLOR = (0, 200, 0)
APPLE_COLOR = (220, 20, 60)
SCORE_COLOR = (255, 255, 255)


def draw_grid(surface, grid_size):
    for x in range(grid_size):
        for y in range(grid_size):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(surface, GRID_COLOR, rect, 1)


def draw_snake(surface, snake):
    for segment in snake:
        rect = pygame.Rect(segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(surface, SNAKE_COLOR, rect)


def draw_apple(surface, apple):
    rect = pygame.Rect(apple[0] * CELL_SIZE, apple[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(surface, APPLE_COLOR, rect)


def draw_score(surface, score, font):
    text = font.render(f"Score: {score}", True, SCORE_COLOR)
    surface.blit(text, (10, 5))
