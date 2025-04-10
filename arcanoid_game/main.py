import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Arcanoid Game')

class Player:
    def __init__(self, paddle_width, paddle_height):
        self.paddle = pygame.Rect(WIDTH // 2 - paddle_width // 2, HEIGHT - 50, paddle_width, paddle_height)

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.paddle.left > 0:
            self.paddle.x -= 5
        if keys[pygame.K_RIGHT] and self.paddle.right < WIDTH:
            self.paddle.x += 5

class Renderer:
    def __init__(self, screen):
        self.screen = screen

    def draw_background(self):
        self.screen.fill((0, 0, 0))  # Fill the screen with black color

    def draw_paddle(self, paddle):
        pygame.draw.rect(self.screen, (255, 255, 255), paddle)

    def draw_ball(self, ball):
        pygame.draw.ellipse(self.screen, (255, 255, 255), ball)

    def draw_bricks(self, bricks):
        for brick in bricks:
            pygame.draw.rect(self.screen, (255, 255, 255), brick)

    def draw_score(self, score):
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))


def main():
    clock = pygame.time.Clock()
    renderer = Renderer(screen)
    score = 0  # Initialize score
    paddle_width, paddle_height = 100, 20
    ball_radius = 10

    player = Player(paddle_width, paddle_height)
    ball = pygame.Rect(WIDTH // 2 - ball_radius, HEIGHT - 70, ball_radius * 2, ball_radius * 2)
    ball_speed = [4, -4]  # X and Y speed of the ball

    # Bricks setup
    bricks = []
    for i in range(5):
        for j in range(10):
            brick = pygame.Rect(i * 80 + 10, j * 30 + 50, 70, 20)
            bricks.append(brick)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        player.move(keys)  # Move paddle using Player class

        # Move the ball
        ball.x += ball_speed[0]
        ball.y += ball_speed[1]

        # Check for ball collisions with walls
        if ball.left <= 0 or ball.right >= WIDTH:
            ball_speed[0] = -ball_speed[0]
        if ball.top <= 0:
            ball_speed[1] = -ball_speed[1]

        # Check for ball collisions with the paddle
        if ball.colliderect(player.paddle):
            ball_speed[1] = -ball_speed[1]

        # Check for ball collisions with bricks
        for brick in bricks[:]:
            if ball.colliderect(brick):
                ball_speed[1] = -ball_speed[1]
                score += 1  # Increase score when a brick is destroyed
                bricks.remove(brick)

        # Render game objects
        renderer.draw_background()  # Draw the background first
        renderer.draw_paddle(player.paddle)
        renderer.draw_ball(ball)
        renderer.draw_bricks(bricks)
        renderer.draw_score(score)

        # Update the display
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()