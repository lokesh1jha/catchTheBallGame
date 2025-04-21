import pygame
import random

pygame.init()

# Set up screen
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Ball")

# Clock for controlling FPS
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Bucket
bucket_width, bucket_height = 100, 20
bucket_x = WIDTH // 2 - bucket_width // 2
bucket_y = HEIGHT - 40
bucket_speed = 7

# Ball
ball_radius = 15
ball_x = random.randint(0, WIDTH - ball_radius)
ball_y = 0
ball_speed = 5

# Score
score = 0
lives = 3
font = pygame.font.SysFont(None, 36)

running = True
while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move bucket
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and bucket_x > 0:
        bucket_x -= bucket_speed
    if keys[pygame.K_RIGHT] and bucket_x < WIDTH - bucket_width:
        bucket_x += bucket_speed

    # Move ball
    # ball_y += score > 20 ? ball_speed * 2 : ball_speed
    if score > 20:
        ball_y = ball_y + (ball_speed * 1.25)
    else:
        ball_y = ball_y + ball_speed

    # Collision check
    if (bucket_y < ball_y + ball_radius < bucket_y + bucket_height and
        bucket_x < ball_x < bucket_x + bucket_width):
        score += 1
        ball_x = random.randint(0, WIDTH - ball_radius)
        ball_y = 0

    # Missed the ball
    if ball_y > HEIGHT:
        lives -= 1
        ball_x = random.randint(0, WIDTH - ball_radius)
        ball_y = 0

    # Draw bucket
    pygame.draw.rect(screen, BLUE, (bucket_x, bucket_y, bucket_width, bucket_height))

    # Draw ball
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    # Draw score and lives
    score_text = font.render(f"Score: {score}  Lives: {lives}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # End game if no lives
    if lives <= 0:
        game_over = font.render("Game Over", True, RED)
        screen.blit(game_over, (WIDTH//2 - 80, HEIGHT//2))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
