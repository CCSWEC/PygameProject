import pygame
import pygame.key
import math
import random
import time

WIDTH, HEIGHT = 1280, 720
BALL_WIDTH, BALL_HEIGHT = 14, 14
BALL_SPEED = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GREY = (64, 64, 64)
RED = (210, 4, 45)

class Ball(pygame.Rect):
    COLOR = WHITE

    def __init__(self, x, y, width, height, angle):
        self.angle = angle
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self, window):
        pygame.draw.circle(window, self.COLOR, self.center, self.width/2)

    def move(self):
        self.x += self.angle.x * BALL_SPEED
        self.y += self.angle.y * BALL_SPEED
        self.y = pygame.math.clamp(self.y, 0, HEIGHT - self.height)
        if self.y == 0 or self.bottom == HEIGHT:
            self.angle.y *= -1
    
    def bounce(self, paddle):
        self.angle.y = (self.centery - paddle.y) / paddle.height - .5 # Set the ball's y direction between [-.5, .5] based on where it collides with the paddle
        self.angle.x = math.copysign(1, self.centerx- paddle.centerx) # Set the ball to move in the opposite direction of the collision
