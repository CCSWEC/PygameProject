import pygame

WIDTH, HEIGHT = 1280, 720
FOOD_WIDTH, FOOD_HEIGHT = 14, 14

class Food(pygame.Rect):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def spawn_food(self):
        pass