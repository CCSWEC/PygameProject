import pygame
import pygame.key
import math
import random
import time
from enum import Enum

CelState = Enum("Normal", "Mine")
class Cel(pygame.Rect):
    def __init__(self, x, y, width, mine):
        self.mine = mine
        self.x = x
        self.y = y
        self.width = width
        self.height = width