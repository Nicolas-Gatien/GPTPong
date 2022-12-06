import sys
import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Pong")

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the paddles
paddle1 = pygame.Rect(20, 150, 10, 100)
paddle2 = pygame.Rect(570, 150, 10, 100)
paddle_shrink_amount = 5

# Set up the ball
ball = pygame.Rect(300, 200, 10, 10)
ball_velocity = [2, -2]
ball_speed_up_counter = 0
ball_speed_up_threshold = 2

# Set up the scores
score1 = 0
score2 = 0

# Set up the clock
clock = pygame.time.Clock()

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the game state
    ball.x += ball_velocity[0]
    ball.y += ball_velocity[1]

    # Handle ball-wall collisions
    if ball.left <= 0:
        ball_velocity[0] *= -1
        score2 += 1
        # Reset the ball's position
        ball.x = 300
        ball.y = 200
        ball_velocity = [2, -2]
        paddle1.height = 100
        paddle2.height = 100

    elif ball.right >= 600:
        ball_velocity[0] *= -1
        score1 += 1
        # Reset the ball's position
        ball.x = 300
        ball.y = 200
        ball_velocity = [-2, 2]
        paddle1.height = 100
        paddle2.height = 100

    if ball.top <= 0 or ball.bottom >= 400:
        ball_velocity[1] *= -1

    # Handle ball-paddle collisions
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_velocity[0] *= -1
        ball_speed_up_counter += 1
        if ball_speed_up_counter % ball_speed_up_threshold == 0:
            ball_velocity[0] *= 1.5
            ball_velocity[1] *= 1.5
        # Shrink the paddles
        paddle1.height -= paddle_shrink_amount
        paddle2.height -= paddle_shrink_amount

    # Handle paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1.y -= 5
    if keys[pygame.K_s]:
        paddle1.y += 5
    if keys[pygame.K_UP]:
        paddle2.y -= 5
    if keys[pygame.K_DOWN]:
        paddle2.y += 5

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.rect(screen, WHITE, ball)

    # Draw the scores
    font = pygame.font.Font(None, 36)
    text = font.render(str(score1), 1, WHITE)
    screen.blit(text, (200, 10))
    text = font.render(str(score2), 1, WHITE)
    screen.blit(text, (400, 10))

    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)