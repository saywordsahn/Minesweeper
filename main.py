import pygame
from enum import Enum
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
pygame.init()
FPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

ROWS = 20
COLS = 20
MINES = 20
PIXELS_PER_CELL = SCREEN_WIDTH / ROWS
red = pygame.Color(50, 50, 50)

class Flag(Enum):
    EMPTY = 1
    BOMB = 2

grid = [[Flag.EMPTY for row in range(ROWS)] for col in range(COLS)]

placed_mines = 0
while placed_mines <= MINES:
    x = random.randint(0, ROWS-1)
    y = random.randint(0, COLS-1)
    if grid[x][y] != Flag.BOMB:
        grid[x][y] = Flag.BOMB
        placed_mines += 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    if event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        print(pos)
        col = int((pos[0] / SCREEN_WIDTH) * ROWS)
        row = int((pos[1] / SCREEN_HEIGHT) * COLS)

        if grid[row][col] == Flag.BOMB:
            print('YOU CLICKED A BOMB')

        print(row, col)



    for i in range(ROWS):
            pygame.draw.line(screen, red, (0, (i + 1) * PIXELS_PER_CELL), (SCREEN_WIDTH, (i + 1) * PIXELS_PER_CELL), 1)

    for i in range(COLS):
            pygame.draw.line(screen, red, ((i + 1) * PIXELS_PER_CELL, 0), ((i + 1) * PIXELS_PER_CELL, SCREEN_HEIGHT), 1)

    pygame.display.update()
    clock.tick(FPS)