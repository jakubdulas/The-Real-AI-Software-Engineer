import pygame
import sys
import random
from grid import *  # Import the grid setup and player functionality
from monster import Monster  # Import the Monster class

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20  # Size of each square in the grid
NUM_MONSTERS = 5  # Number of monsters to spawn
PLAYER_HEALTH = 100  # Player health

# Load sounds
# attack_sound = pygame.mixer.Sound('assets/attack_sound.wav')

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Monster Fighting Game")

# Player position
player_pos = [GRID_SIZE, GRID_SIZE]  # Starting grid position
player_health = PLAYER_HEALTH  # Initial player health

# Create monsters
monsters = []
for _ in range(NUM_MONSTERS):
    x = random.randint(0, (SCREEN_WIDTH // GRID_SIZE) - 1) * GRID_SIZE
    y = random.randint(0, (SCREEN_HEIGHT // GRID_SIZE) - 1) * GRID_SIZE
    monsters.append(Monster(x, y, health=100))  # Each monster starts with 100 health

# Tree positions
num_trees = 10
tree_positions = []
for _ in range(num_trees):
    x = random.randint(0, (SCREEN_WIDTH // GRID_SIZE) - 1) * GRID_SIZE
    y = random.randint(0, (SCREEN_HEIGHT // GRID_SIZE) - 1) * GRID_SIZE
    tree_positions.append((x, y))

# Function to draw health bars


def draw_health_bars(screen, player_health, monsters):
    # Player health bar
    pygame.draw.rect(screen, (0, 255, 0), (10, 10, 200, 20))  # Background
    pygame.draw.rect(
        screen, (255, 0, 0), (10, 10, 200 * (player_health / PLAYER_HEALTH), 20)
    )  # Health bar

    # Monster health bars
    for i, monster in enumerate(monsters):
        pygame.draw.rect(screen, (0, 0, 255), (10, 40 + i * 30, 200, 20))  # Background
        pygame.draw.rect(
            screen, (255, 0, 0), (10, 40 + i * 30, 200 * (monster.health / 100), 20)
        )  # Health bar


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle player attack (spacebar)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            for monster in monsters:
                if player_pos[0] == monster.x and player_pos[1] == monster.y:
                    monster.health -= 10  # Damage to the monster
                    # attack_sound.play()  # Play the attack sound
                    if monster.health <= 0:
                        monsters.remove(monster)  # Remove the monster if defeated

    # Handle player movement
    handle_player_movement(player_pos, screen, GRID_SIZE)

    # Fill the background
    screen.fill((0, 0, 0))

    # Draw the grid
    draw_grid(screen, GRID_SIZE)

    # Draw trees
    draw_trees(screen, tree_positions, GRID_SIZE)

    # Draw the player
    pygame.draw.rect(
        screen, (0, 0, 255), (player_pos[0], player_pos[1], GRID_SIZE, GRID_SIZE)
    )

    # Move monsters and draw them
    for monster in monsters:
        monster.move_towards(player_pos)
        monster.draw(screen)
        # Check for collision with the hero
        if monster.x == player_pos[0] and monster.y == player_pos[1]:
            print("Game Over! The monster reached the hero.")
            running = False

    # Draw health bars
    draw_health_bars(screen, player_health, monsters)

    # Update the display
    pygame.display.flip()

# Clean up
pygame.quit()
sys.exit()
