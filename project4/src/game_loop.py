"""
Module: game_loop.py
Handles the game lifecycle and primary loop control.
"""

import pygame

class GameLoop:
    """Class that manages the main game loop lifecycle."""
    def __init__(self, game, renderer, input_handler, fps=10):
        self.game = game
        self.renderer = renderer
        self.input_handler = input_handler
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.running = True

    def run(self):
        """Run the primary game loop."""
        while self.running:
            self.input_handler.handle_events(self)
            self.game.update()
            self.renderer.render(self.game)
            pygame.display.flip()
            self.clock.tick(self.fps)

    def stop(self):
        """Stop the game loop."""
        self.running = False
