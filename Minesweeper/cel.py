import pygame
import pygame.key
import math
import random
import time
from collections import namedtuple
from enum import Enum

class CelState(Enum):
    Normal = 1
    Mine = 2

# Cel clear effect constants
MINE_CLEAR_WAIT_TIME = 3

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GREY = (64, 64, 64)
RED = (210, 4, 45)

gridPosition = namedtuple('gridPosition', ['x', 'y'])

class Cel(pygame.Rect):
    COLOR = WHITE

    def __init__(self, x, y, width):
        self.clearWaitTime = MINE_CLEAR_WAIT_TIME
        self.state = CelState.Normal
        self.gridPosition = gridPosition(x=x, y=y)
        self.adjacentMines = 0
        self.hidden = True
        self.clearCascading = False
        self.flagged = False
        self.x = (width + 2) * x 
        self.y = (width + 2) * y
        self.width = width
        self.height = width

    def update(self, mineArray):
        self.clearWaitTime -= 1
        if (self.clearWaitTime <= 0):
            self.clear(mineArray)

    def draw(self, window):
        pygame.draw.rect(window, self.COLOR, self)

    def clear(self, mineArray):
        if (self.flagged or not self.hidden): return

        self.hidden = False
        if self.state == CelState.Mine:
            self.COLOR = RED
        else:
            self.COLOR = DARK_GREY

        for y in [-1, 1]:
            if (self.gridPosition.y + y == -1 or self.gridPosition.y + y == len(mineArray)): continue
            mine = mineArray[self.gridPosition.y + y][self.gridPosition.x]
            if (mine.adjacentMines == 0 and mine.hidden and not mine.clearCascading):
                mine.clearCascading = True
            mineArray[self.gridPosition.y + y][self.gridPosition.x] = mine

        for x in [-1, 1]:
            if (self.gridPosition.x + x == -1 or self.gridPosition.x + x == len(mineArray[0])): continue
            mine = mineArray[self.gridPosition.y][self.gridPosition.x + x]
            if (mine.adjacentMines == 0 and mine.hidden and not mine.clearCascading):
                mine.clearCascading = True
            mineArray[self.gridPosition.y][self.gridPosition.x + x] = mine

    def setCelNumber(self, mineArray):
        for y in [-1,0,1]:
            if (self.gridPosition.y + y == -1 or self.gridPosition.y + y == len(mineArray)): continue
            for x in [-1,0,1]:
                if ((y == 0 and x == 0) or(self.gridPosition.x + x == -1 or self.gridPosition.x + x == len(mineArray[0]))): continue
                mineArray[self.gridPosition.y + y][self.gridPosition.x + x].adjacentMines += 1
