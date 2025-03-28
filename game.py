import pygame
import pygame.key
import math
import random
import time

from pong.PongGame import PongGame
from Minesweeper.minesweeperGame import MinesweeperGame

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
pygame.display.set_caption('Choose a Game!')

# Setup Pause Effect
PAUSE_DARKEN = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
PAUSE_DARKEN.fill((0, 0, 0, 160))

# Setup Game List
GAME_LIST = {
    pygame.K_1: PongGame,
    pygame.K_2: MinesweeperGame
} # Add games to list as: [key that selects the game: the class of the game to load]

# Initialize fps
FPS = 60

# Function for drawing on the screen
def draw(window, game):
    window.fill(DARK_GREY)
    if (game):
        game.draw(window)

        if (not game.running):
            window.blit(PAUSE_DARKEN, (0, 0))
            selectText = "GAME PAUSED:\nEsc: Resume\n1: Reset Game\n2: Exit to Game Select"
            lines = selectText.splitlines()
            for line in range(len(lines)):
                text = FONT.render(lines[line], True, WHITE)
                window.blit(text, (0, HEIGHT/2+50*line, WIDTH, HEIGHT/2-50*line))
    else:    
        selectText = "Pick a Game (Press Number):\n1. Pong\n2. Mindsweeper (NOT YET)\n(press ESC to pause)"
        lines = selectText.splitlines()
        for line in range(len(lines)):
            text = FONT.render(lines[line], True, WHITE)
            window.blit(text, (0, HEIGHT/2+50*line, WIDTH, HEIGHT/2-50*line))

    pygame.display.update()

# Main function
def main():
    running = True
    clock = pygame.time.Clock()
    game = None

    # Game loop
    while running:
        draw(WINDOW, game)
        if (game and game.running):
            game.main()

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # when user clicks x, closes game
                running = False
            if (game):
                game.event(event)
                if event.type == pygame.KEYDOWN:
                    if (game.running):
                        if event.key == pygame.K_ESCAPE:
                            game.running = False
                            pygame.display.set_caption('Game Paused!')
                    else:
                        if event.key == pygame.K_ESCAPE:
                            game.running = True
                            pygame.display.set_caption(game.caption)
                        if (event.key == pygame.K_1):
                            game = type(game)()
                            break
                        if (event.key == pygame.K_2):
                            game = None
                            pygame.display.set_caption('Choose a Game!')
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key in GAME_LIST:
                        game = GAME_LIST[event.key]()
                        pygame.display.set_caption(game.caption) # set the window caption for the game in its class file
    pygame.quit()

# Calling main 
if __name__ == "__main__":
    main()


