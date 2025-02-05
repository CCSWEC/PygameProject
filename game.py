import pygame

pygame.init()

running = True

# Widths, heights and speeds
WIDTH, HEIGHT = 1280, 720
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
PADDLE_SPEED = 10
BALL_SPEED = 5

# Colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)
DARK_GREY = (64, 64, 64)


# Setup screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

# Initialize clock and FPS
clock = pygame.time.Clock()
FPS = 60

# Paddle class
class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
    
    def move(self, up_key, down_key):
        key = pygame.key.get_pressed()

        if key[up_key]:
            self.rect.y += PADDLE_SPEED

        if key[down_key]:
            self.rect.y -= PADDLE_SPEED

    
    # Method for drawing the paddle

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # when user clicks x, closes game
            running = False

    # Fill screen white
    screen.fill(DARK_GREY)

    # Render game here

    pygame.display.update()

    # limit fps to 60
    clock.tick(FPS)

pygame.quit()


