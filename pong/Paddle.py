import pygame
import pygame.key
import math

WIDTH, HEIGHT = 1280, 720
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 125
PADDLE_OFFSET = 35
PADDLE_SPEED = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GREY = (64, 64, 64)
RED = (210, 4, 45)

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
