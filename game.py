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

FONT = pygame.font.Font(None, 50)
# Setup screen
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

# Initialize fps
FPS = 60

# Function for drawing on the screen
def draw(window, game):
    window.fill(DARK_GREY)
    if (game):
        game.draw(window)
    else:
        selectText = "Pick a Game (Press Number):\n1. Pong\n2. Mindsweeper (NOT YET)\n(press ESC to exit a game)"
        lines = selectText.splitlines()
        for line in range(lines.__len__()):
            text = FONT.render(lines[line], True, WHITE)
            window.blit(text, (0, HEIGHT/2+50*line, WIDTH, HEIGHT/2-50*line))

    pygame.display.update()

# Main function
def main():
    running = True
    clock = pygame.time.Clock()
    game = None
    # Make Paddles and put them in a list

    # Game loop
    while running:
        draw(WINDOW, game)
        if (game):
            game.main()

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # when user clicks x, closes game
                running = False
            if (game):
                game.event(event)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game = None
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        game = PongGame()
    pygame.quit()

# Calling main 
if __name__ == "__main__":
    main()


