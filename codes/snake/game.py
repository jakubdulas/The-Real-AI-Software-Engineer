# game.py

import pygame
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, GREEN, RED

# Initialize Pygame
pygame.init()

# Set up display
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')


class Snake:
    def __init__(self):
        self.body = [[100, 50], [90, 50], [80, 50]]  # Initial position
        self.direction = 'RIGHT'
        self.grow = False

    def move(self):
        # Determine new head position
        head_x, head_y = self.body[0]
        if self.direction == 'RIGHT':
            head_x += 10
        elif self.direction == 'LEFT':
            head_x -= 10
        elif self.direction == 'UP':
            head_y -= 10
        elif self.direction == 'DOWN':
            head_y += 10
        
        # Insert new position
        self.body.insert(0, [head_x, head_y])
        
        # If grow is not triggered, remove the last segment
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False  # Reset grow flag

    def change_direction(self, new_direction):
        # Avoid reverse direction
        if (new_direction == 'LEFT' and self.direction != 'RIGHT') or \
           (new_direction == 'RIGHT' and self.direction != 'LEFT') or \
           (new_direction == 'UP' and self.direction != 'DOWN') or \
           (new_direction == 'DOWN' and self.direction != 'UP'):
            self.direction = new_direction

    def grow_snake(self):
        self.grow = True

class Food:
    def __init__(self):
        self.position = [random.randrange(1, (SCREEN_WIDTH // 10)) * 10,
                         random.randrange(1, (SCREEN_HEIGHT // 10)) * 10]
    
    def spawn_food(self):
        self.position = [random.randrange(1, (SCREEN_WIDTH // 10)) * 10,
                         random.randrange(1, (SCREEN_HEIGHT // 10)) * 10]

# Main game loop
def game_loop():
    snake = Snake()
    food = Food()
    clock = pygame.time.Clock()
    score = 0

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction('UP')
                elif event.key == pygame.K_DOWN:
                    snake.change_direction('DOWN')
                elif event.key == pygame.K_LEFT:
                    snake.change_direction('LEFT')
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction('RIGHT')

        # Move the snake
        snake.move()

        # Check for collisions with food
        if snake.body[0] == food.position:
            snake.grow_snake()
            food.spawn_food()
            score += 1
        
        # Check for collisions with walls or self
        if (snake.body[0][0] < 0 or snake.body[0][0] >= SCREEN_WIDTH or
                snake.body[0][1] < 0 or snake.body[0][1] >= SCREEN_HEIGHT or
                snake.body[0] in snake.body[1:]):
            print("Game Over! Score:", score)
            pygame.quit()
            return

        # Clear the screen
        window.fill(BLACK)

        # Draw the snake
        for segment in snake.body:
            pygame.draw.rect(window, GREEN, pygame.Rect(segment[0], segment[1], 10, 10))

        # Draw the food
        pygame.draw.rect(window, RED, pygame.Rect(food.position[0], food.position[1], 10, 10))

        # Refresh the screen
        pygame.display.flip()

        # Control the game's frame rate
        clock.tick(15)

if __name__ == "__main__":
    game_loop()