import pygame
import pygame.key
import math

pygame.init()

# Widths, heights and speeds
WIDTH, HEIGHT = 1280, 720
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 125
BALL_WIDTH, BALL_HEIGHT = 14, 14
PADDLE_OFFSET = 35
PADDLE_SPEED = 10
BALL_SPEED = 5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GREY = (64, 64, 64)
RED = (210, 4, 45)

# Setup screen
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

# Initialize fps
FPS = 60

# Paddle class
class Paddle:
    COLOR = WHITE

    def __init__(self, x, y, width, height, controls):
        self.controls = controls # The Up and Down control key for the paddle
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    # Function to draw the paddles
    def draw(self, window):
        pygame.draw.rect(window, self.COLOR, (self.x, self.y, PADDLE_WIDTH, PADDLE_HEIGHT))

    # Function to move paddles
    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[self.controls[0]]:
            self.y -= PADDLE_SPEED
        if pressed[self.controls[1]]:
            self.y += PADDLE_SPEED
        self.y = pygame.math.clamp(self.y, 0, HEIGHT-PADDLE_HEIGHT)

# Ball Class (B)
class Ball:
    COLOR = WHITE

    def __init__(self, x, y, width, height):
        self.angle = pygame.Vector2(1,0)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self, window):
        pygame.draw.rect(window, self.COLOR, (self.x, self.y, BALL_WIDTH, BALL_HEIGHT))

    def move(self):
        pass
    def isColliding(self, paddles) -> bool:
        return pygame.Rect(self.x, self.y, self.width, self.height).collidelist(paddles)
    def bounce(self, paddle):
        self.angle.y = (self.y - (paddle.y + PADDLE_HEIGHT)) // (paddle.y - (paddle.y + PADDLE_HEIGHT)) - .5
        # self.angle.x = mat

# Class to keep the score
class ScoreBoard:
    COLOR = WHITE

    def __init__(self, window, width, height):
        self.window = window
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, 50)
        self.player1_score = 0
        self.player2_score = 0

    # Update scores
    def update_score(self, player1, player2):
        self.player1_score = player1
        self.player2_score = player2

    
#Border for Ball to bounce off of 
class Border:
    COLOR = WHITE
    

# Function for drawing on the screen
def draw(window, paddles, ball):
    window.fill(DARK_GREY)

    for y in range(HEIGHT//48, HEIGHT, HEIGHT//12):
        pygame.draw.line(window, WHITE, (WIDTH // 2, y), (WIDTH // 2, y + HEIGHT//24), 4)
    
    for paddle in paddles:
        paddle.draw(WINDOW)

    ball.draw(WINDOW)
    pygame.display.update()

# Main function
def main():
    running = True
    clock = pygame.time.Clock()

    # Make Paddles and put them in a list
    right_paddle = Paddle(PADDLE_OFFSET, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT, [pygame.K_UP, pygame.K_DOWN])
    left_paddle = Paddle(WIDTH - PADDLE_OFFSET - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT, [pygame.K_w, pygame.K_s])
    paddles = [right_paddle, left_paddle]

    # Make ball
    ball = Ball(WIDTH // 2 - BALL_WIDTH//2, HEIGHT // 2 - BALL_HEIGHT // 2, BALL_WIDTH, BALL_HEIGHT)

    # Game loop
    while running:
        draw(WINDOW, paddles, ball)
        for paddle in paddles:
            paddle.move()
            
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # when user clicks x, closes game
                running = False

    pygame.quit()

# Calling main 
if __name__ == "__main__":
    main()


