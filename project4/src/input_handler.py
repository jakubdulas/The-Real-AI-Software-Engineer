"""
Module: input_handler.py
Handles user input for the Snake game.
"""

import pygame

class InputHandler:
    """Handles keyboard input and maps it to game actions."""
    def handle_events(self, game_loop):
        """Process pygame events and update game or game loop accordingly."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_loop.stop()
            elif event.type == pygame.KEYDOWN:
                self.handle_direction_keys(event.key, game_loop.game)

    def handle_direction_keys(self, key, game):
        """Handle arrow key presses for changing snake's direction."""
        direction_map = {
            pygame.K_UP:    (0, -1),
            pygame.K_DOWN:  (0, 1),
            pygame.K_LEFT:  (-1, 0),
            pygame.K_RIGHT: (1, 0),
        }
        if key in direction_map:
            game.snake.set_direction(direction_map[key])
