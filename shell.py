import pygame

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
pygame.init()
FPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    pygame.display.update()
    clock.tick(FPS)