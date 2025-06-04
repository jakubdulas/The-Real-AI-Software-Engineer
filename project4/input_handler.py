import pygame

class InputHandler:
    def __init__(self):
        self.direction_map = {
            pygame.K_UP: 'UP',
            pygame.K_DOWN: 'DOWN',
            pygame.K_LEFT: 'LEFT',
            pygame.K_RIGHT: 'RIGHT'
        }

    def process_events(self, game_over, snake, initial_pos, restart_callback):
        """
        Handles all input events and updates snake direction or triggers restart via callback.
        Returns True if the game should continue running, False if a quit event was received.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key in self.direction_map and not game_over:
                    snake.set_direction(self.direction_map[event.key])
                if event.key == pygame.K_r and game_over:
                    restart_callback()
        return True
