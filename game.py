import pygame
import pygame.key
import math
import random
import time

pygame.init()

# Widths, heights and speeds
WIDTH, HEIGHT = 1280, 720
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 125
BALL_WIDTH, BALL_HEIGHT = 14, 14
PADDLE_OFFSET = 35
PADDLE_SPEED = 10
BALL_SPEED = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GREY = (64, 64, 64)
RED = (210, 4, 45)

# Setup screen
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

# Initialize fps
FPS = 60

# Paddle class
class Paddle(pygame.Rect):
    COLOR = WHITE

    def __init__(self, x, y, width, height, controls):
        self.controls = controls # The Up and Down control key for the paddle
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    # Function to draw the paddles
    def draw(self, window):
        pygame.draw.rect(window, self.COLOR, self)

    # Function to move paddles
    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[self.controls[0]]:
            self.y -= PADDLE_SPEED
        if pressed[self.controls[1]]:
            self.y += PADDLE_SPEED
        self.y = pygame.math.clamp(self.y, 0, HEIGHT-PADDLE_HEIGHT)

# Ball Class (B)
class Ball(pygame.Rect):
    COLOR = WHITE

    def __init__(self, x, y, width, height, angle):
        self.angle = angle
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self, window):
        pygame.draw.rect(window, self.COLOR, self)

    def move(self):
        self.x += self.angle.x * BALL_SPEED
        self.y += self.angle.y * BALL_SPEED
        self.y = pygame.math.clamp(self.y, 0, HEIGHT - self.height)
        if self.y == 0 or self.bottom == HEIGHT:
            self.angle.y *= -1
    
    def bounce(self, paddle):
        self.angle.y = (self.centery - paddle.y) / paddle.height - .5 # Set the ball's y direction between [-.5, .5] based on where it collides with the paddle
        self.angle.x = math.copysign(1, self.centerx- paddle.centerx) # Set the ball to move in the opposite direction of the collision

# Class to keep the score
class ScoreBoard:
    COLOR = WHITE

    def __init__(self, window, width, height):
        self.window = window
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, 150)
        self.player1_score = 0
        self.player2_score = 0

    # Update scores
    def update_score(self, player1, player2):
        self.player1_score = player1
        self.player2_score = player2

    def increase_score(self, player):
        if player == 1:
            self.player1_score += 1
        elif player == 2:
            self.player2_score += 1

    def draw(self):
        p1_text = self.font.render(str(self.player1_score), True, WHITE)
        p2_text = self.font.render(str(self.player2_score), True, WHITE)

        p1_rect = p1_text.get_rect(center=(self.width // 2 - 100, 50))
        p2_rect = p2_text.get_rect(center=(self.width // 2 + 100, 50))

        self.window.blit(p1_text, p1_rect)
        self.window.blit(p2_text, p2_rect)

    
#Border for Ball to bounce off of 
class Border:
    COLOR = WHITE
    

# Function for drawing on the screen
def draw(window, paddles, balls, scoreboard):
    window.fill(DARK_GREY)

    for y in range(HEIGHT//48, HEIGHT, HEIGHT//12):
        pygame.draw.line(window, WHITE, (WIDTH // 2, y), (WIDTH // 2, y + HEIGHT//24), 4)
    
    for paddle in paddles:
        paddle.draw(WINDOW)

    for ball in balls:
        ball.draw(WINDOW)

    scoreboard.draw()

    
    pygame.display.update()

# Main function
def main():
    running = True
    clock = pygame.time.Clock()

    # Make Paddles and put them in a list
    right_paddle = Paddle(PADDLE_OFFSET, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT, [pygame.K_w, pygame.K_s])
    left_paddle = Paddle(WIDTH - PADDLE_OFFSET - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT, [pygame.K_UP, pygame.K_DOWN])
    paddles = [right_paddle, left_paddle]

    balls = [] # Initialize ball array

    scoreboard = ScoreBoard(WINDOW, WIDTH, HEIGHT)

    # Game loop
    while running:
        draw(WINDOW, paddles, balls, scoreboard)

        for paddle in paddles:
            paddle.move()

        for ball in balls:
            ball.move()
            if ball.collidelist(paddles) != -1:
                ball.bounce(paddles[ball.collidelist(paddles)])

            if ball.centerx < 0:  # Right player scores
                scoreboard.increase_score(2)
                balls.remove(ball)
            elif ball.centerx > WIDTH:  # Left player scores
                scoreboard.increase_score(1)
                balls.remove(ball)

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # when user clicks x, closes game
                running = False
            if len(balls) == 0:
                time.sleep(.10) # wait one decisecond before being able to spawn a ball
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        balls.append(
                            Ball(WIDTH // 2 - BALL_WIDTH//2, HEIGHT // 2 - BALL_HEIGHT // 2, BALL_WIDTH, BALL_HEIGHT, 
                                pygame.Vector2(random.choice([-1, 1]) , random.random() - .5))
                                )

    pygame.quit()

# Calling main 
if __name__ == "__main__":
    main()


