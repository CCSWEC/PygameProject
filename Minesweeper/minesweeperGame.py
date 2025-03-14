import pygame
import pygame.key
import math
import random
import time
from .cel import Cel

MINE_SIZE = 20
MINE_GRID_WIDTH, MINE_GRID_HEIGHT = 15, 15
pygame.display.set_caption('Pong')

# Initialize fps
FPS = 60

class PongGame:
    # Main function
    def __init__(self):
        self.running = True

        self.mineArray[MINE_GRID_HEIGHT][MINE_GRID_WIDTH]  # Initialize mine array

        for y in range(MINE_GRID_HEIGHT):
            for x in range(MINE_GRID_WIDTH):
                self.mineArray[y][x] = Cel(MINE_SIZE * (x+1))
        
    # Function for drawing on the screen
    def draw(self, window):
        

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
