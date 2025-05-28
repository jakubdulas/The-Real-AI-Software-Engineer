"""
Module: renderer.py
Handles drawing game entities and the grid to the screen.
"""

import pygame

class Renderer:
    """Handles rendering of the game state to the Pygame window."""
    def __init__(self, screen, cell_size, grid_width, grid_height):
        self.screen = screen
        self.cell_size = cell_size
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.font = pygame.font.SysFont("Arial", 24)

    def render(self, game):
        """Render the game state and handle game over screen if necessary."""
        self.screen.fill((0, 0, 0))
        self._draw_grid()
        game.draw(self.screen, self.cell_size)
        self._draw_score(game.score)
        if getattr(game, 'game_over', False):
            self._draw_game_over(game.score)

    def _draw_game_over(self, score):
        overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        self.screen.blit(overlay, (0, 0))
        go_font = pygame.font.SysFont("Arial", 42, bold=True)
        msg = f"Game Over! Score: {score}"
        surf = go_font.render(msg, True, (255, 80, 80))
        rect = surf.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2 - 20))
        self.screen.blit(surf, rect)
        instruction = self.font.render("Press ESC to quit or R to restart", True, (255, 255, 255))
        inst_rect = instruction.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2 + 24))
        self.screen.blit(instruction, inst_rect)

    def _draw_grid(self):
        """Draws the background grid."""
        for x in range(self.grid_width):
            for y in range(self.grid_height):
                rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, (40, 40, 40), rect, 1)

    def _draw_score(self, score):
        """Draws the player's score in the upper left corner in a dedicated band."""
        # Draw a filled rectangle as the background for score
        score_bg_rect = pygame.Rect(0, 0, self.screen.get_width(), 38)
        pygame.draw.rect(self.screen, (24, 24, 24), score_bg_rect)
        # Draw the score text
        surf = self.font.render(f"Score: {score}", True, (220, 220, 220))
        self.screen.blit(surf, (14, 8))
