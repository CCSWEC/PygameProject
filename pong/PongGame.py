import pygame
import pygame.key
import math
import random
import time
from .Ball import Ball
from .Paddle import Paddle
from .ScoreBoard import ScoreBoard

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

class PongGame:
    # Function for drawing on the screen
    def draw(self, window):
        for y in range(HEIGHT//48, HEIGHT, HEIGHT//12):
            pygame.draw.line(window, WHITE, (WIDTH // 2, y), (WIDTH // 2, y + HEIGHT//24), 4)
        
        for paddle in self.paddles:
            paddle.draw(WINDOW)

        for ball in self.balls:
            ball.draw(WINDOW)

        self.scoreboard.draw()

    # Main function
    def __init__(self):
        self.running = True

        # Make Paddles and put them in a list
        self.right_paddle = Paddle(PADDLE_OFFSET, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT, [pygame.K_w, pygame.K_s])
        self.left_paddle = Paddle(WIDTH - PADDLE_OFFSET - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT, [pygame.K_UP, pygame.K_DOWN])
        self.paddles = [self.right_paddle, self.left_paddle]

        self.balls = [] # Initialize ball array

        self.scoreboard = ScoreBoard(WINDOW, WIDTH, HEIGHT)

        # Game loop
    def main(self):
        for paddle in self.paddles:
            paddle.move()

        for ball in self.balls:
            ball.move()
            if ball.collidelist(self.paddles) != -1:
                ball.bounce(self.paddles[ball.collidelist(self.paddles)])

            if ball.centerx < 0:  # Right player scores
                self.scoreboard.increase_score(2)
                self.balls.remove(ball)
            elif ball.centerx > WIDTH:  # Left player scores
                self.scoreboard.increase_score(1)
                self.balls.remove(ball)

    def event(self, event):
       if len(self.balls) == 0:
        #time.sleep(.10) # wait one decisecond before being able to spawn a ball
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.balls.append(
                    Ball(WIDTH // 2 - BALL_WIDTH//2, HEIGHT // 2 - BALL_HEIGHT // 2, BALL_WIDTH, BALL_HEIGHT, 
                        pygame.Vector2(random.choice([-1, 1]) , random.random() - .5))
                        )



