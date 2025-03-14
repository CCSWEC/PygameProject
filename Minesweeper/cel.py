import pygame
import pygame.key
import math
import random
import time
from enum import Enum

CelState = Enum("Normal", "Mine")
class Cel(pygame.Rect):
    def __init__(self, x, y, width):
        self.state = CelState.Normal
        self.gridPosition = {x:0,y:0}
        self.adjacentMines = 0
        self.hidden = True
        self.flagged = False
        self.x = x
        self.y = y
        self.width = width
        self.height = width
    
    def main(self):
        pass
    def draw(self, window):
        pygame.draw.rect(window, self.COLOR, self)
    def clear(self, mineArray):
        self.hidden = False
        for y in range(3):
            for x in range(3):
                if (mineArray[self.gridPosition.y + y-1][self.gridPosition.x + x-1].adjacentMines == 0):
                    mineArray[self.gridPosition.y + y-1][self.gridPosition.x + x-1].clear(mineArray)

    def setCelNumber(self, mineArray):
        for y in range(3):
            for x in range(3):
                if ((y == 1 and x == 1) 
                    or (self.gridPosition.y + y-1 == -1 or self.gridPosition.y + y-1 == len(mineArray))
                    or (self.gridPosition.x + x-1 == -1 or self.gridPosition.x + x-1 == len(mineArray[0]))): continue
                mineArray[self.gridPosition.y + y-1][self.gridPosition.x + x-1].adjacentMines += 1
