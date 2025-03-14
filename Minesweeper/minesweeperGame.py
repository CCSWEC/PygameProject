import pygame
import pygame.key
import math
import random
import time
from .cel import Cel
from .cel import CelState

MINE_SIZE = 40
MINE_GRID_WIDTH, MINE_GRID_HEIGHT = 15, 15
MINE_COUNT = 40

class MinesweeperGame:
    # Main function
    def __init__(self):
        self.running = True
        self.mineArray = []
        self.setMines()

    def setMines(self):
        self.mineArray = []
        for y in range(MINE_GRID_HEIGHT):
            col = []
            for x in range(MINE_GRID_WIDTH):
                col.append(Cel(x, y, MINE_SIZE)) # Initialize mine array
            self.mineArray.append(col)

        for i in range(MINE_COUNT):
            randX = random.randint(0, len(self.mineArray[0])-1)
            randY = random.randint(0, len(self.mineArray)-1)

            while (self.mineArray[randY][randX].state == CelState.Mine):
                randX = random.randint(0, len(self.mineArray[0])-1)
                randY = random.randint(0, len(self.mineArray)-1)

            self.mineArray[randY][randX].state = CelState.Mine
            self.mineArray[randY][randX].adjacentMines = 1

        for col in self.mineArray:
            for mine in col:
                if (mine.state == CelState.Mine):
                    mine.setCelNumber(self.mineArray)
        
    # Function for drawing on the screen
    def draw(self, window):
        for col in self.mineArray:
            for mine in col:
                mine.draw(window)

        # Game loop
    def main(self):
        pass

    def event(self, event):
       leftMouse, _, rightMouse = pygame.mouse.get_pressed()
       for col in self.mineArray:
            for mine in col:
                if (event.type == pygame.MOUSEBUTTONDOWN and mine.collidepoint(pygame.mouse.get_pos())):
                    if leftMouse:
                        mine.clear(self.mineArray)
                    elif rightMouse:
                        mine.flagged = not mine.flagged
