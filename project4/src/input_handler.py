import pygame

DIRECTION_LOOKUP = {
    pygame.K_UP: (0, -1),
    pygame.K_DOWN: (0, 1),
    pygame.K_LEFT: (-1, 0),
    pygame.K_RIGHT: (1, 0),
}

def get_direction_from_event(event):
    if event.type == pygame.KEYDOWN:
        return DIRECTION_LOOKUP.get(event.key)
    return None
