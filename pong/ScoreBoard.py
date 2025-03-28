import pygame
import pygame.key
import math
import random
import time

# Colors
WHITE = (255, 255, 255)

class ScoreBoard:
    COLOR = WHITE

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, 150)
        self.player1_score = 0
        self.player2_score = 0

    # Update scores
    def update_score(self, player1, player2):
        self.player1_score = player1
        self.player2_score = player2

    def increase_score(self, player):
        if player == 1:
            self.player1_score += 1
        elif player == 2:
            self.player2_score += 1

    def draw(self, window):
        p1_text = self.font.render(str(self.player1_score), True, WHITE)
        p2_text = self.font.render(str(self.player2_score), True, WHITE)

        p1_rect = p1_text.get_rect(center=(self.width // 2 - 100, 50))
        p2_rect = p2_text.get_rect(center=(self.width // 2 + 100, 50))

        window.blit(p1_text, p1_rect)
        window.blit(p2_text, p2_rect)

    