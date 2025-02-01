import pygame
pygame.init()

WIDTH, HEIGHT = 1280, 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # when user clicks x, closes game
            running = False

    # Fill screen white
    screen.fill("white")

    # Render game here

    pygame.display.flip()

    # limit fps to 60
    clock.tick(60)

pygame.quit()


