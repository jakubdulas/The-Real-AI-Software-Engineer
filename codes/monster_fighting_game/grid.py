import pygame

# Function to draw the grid

def draw_grid(screen, grid_size):
    # Draw vertical lines
    for x in range(0, screen.get_width(), grid_size):
        pygame.draw.line(screen, (255, 255, 255), (x, 0), (x, screen.get_height()))
    # Draw horizontal lines
    for y in range(0, screen.get_height(), grid_size):
        pygame.draw.line(screen, (255, 255, 255), (0, y), (screen.get_width(), y))

# Function to get the player movement (WASD)

def handle_player_movement(player_pos, screen, grid_size):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:  # Move left
        player_pos[0] -= grid_size
    if keys[pygame.K_d]:  # Move right
        player_pos[0] += grid_size
    if keys[pygame.K_w]:  # Move up
        player_pos[1] -= grid_size
    if keys[pygame.K_s]:  # Move down
        player_pos[1] += grid_size

    # Keep within bounds
    player_pos[0] = max(0, min(player_pos[0], screen.get_width() - grid_size))
    player_pos[1] = max(0, min(player_pos[1], screen.get_height() - grid_size))

# Function to draw trees

def draw_trees(screen, tree_positions, grid_size):
    for pos in tree_positions:
        pygame.draw.rect(screen, (0, 255, 0), (pos[0], pos[1], grid_size, grid_size))  # Draw a green tree