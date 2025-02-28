import pygame
import pygame.key
import math
import random
import time
from pong.Ball import Ball
from pong.Paddle import Paddle
from pong.PongGame import PongGame
from pong.ScoreBoard import ScoreBoard
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

# Function for drawing on the screen
def draw(window):
    window.fill(DARK_GREY)
    
    pygame.display.update()

# Main function
def main():
    game = None
    running = True
    clock = pygame.time.Clock()

    # Make Paddles and put them in a list
    game = PongGame()

    # Game loop
    while running:
        game.main()

        # for paddle in paddles:
        #     paddle.move()

        # for ball in balls:
        #     ball.move()
        #     if ball.collidelist(paddles) != -1:
        #         ball.bounce(paddles[ball.collidelist(paddles)])

        #     if ball.centerx < 0:  # Right player scores
        #         scoreboard.increase_score(2)
        #         balls.remove(ball)
        #     elif ball.centerx > WIDTH:  # Left player scores
        #         scoreboard.increase_score(1)
        #         balls.remove(ball)

        clock.tick(FPS)

        game.event()
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT: # when user clicks x, closes game
        #         running = False
        #     if len(balls) == 0:
        #         time.sleep(.10) # wait one decisecond before being able to spawn a ball
        #         if event.type == pygame.KEYDOWN:
        #             if event.key == pygame.K_SPACE:
        #                 balls.append(
        #                     Ball(WIDTH // 2 - BALL_WIDTH//2, HEIGHT // 2 - BALL_HEIGHT // 2, BALL_WIDTH, BALL_HEIGHT, 
        #                         pygame.Vector2(random.choice([-1, 1]) , random.random() - .5))
        #                         )
    pygame.quit()

# Calling main 
if __name__ == "__main__":
    main()


