import pygame

pygame.init()

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
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

# Initialize fps
FPS = 60

def draw(window):
    window.fill(DARK_GREY)
    pygame.display.update()

# Paddle class
class Paddle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    # Method for drawing the paddle

def main():
    running = True
    clock = pygame.time.Clock()

    while running:
        draw(WINDOW)
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # when user clicks x, closes game
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()


