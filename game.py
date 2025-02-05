import pygame

pygame.init()

running = True

WIDTH, HEIGHT = 1280, 720
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
PADDLE_SPEED = 10
WHITE = (255, 255, 255)
BLACK = (0,0,0)

# Setup screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()
FPS = 60

# Paddle class
class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
    
    # Method for moving

    # Method for drawing the paddle

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # when user clicks x, closes game
            running = False

    # Fill screen white
    screen.fill("white")

    # Render game here

    pygame.display.flip()

    # limit fps to 60
    clock.tick(FPS)

pygame.quit()


