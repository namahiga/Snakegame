import random
import sys
import pygame
from pygame.locals import *
pygame.init() #initializing pygame
pygame.display.set_caption("snake game")
#Global Variables
rows = 25
width = 500
height = 500
w = 500
MARGIN = 0
surface = pygame.display.set_mode((500, 500))
#player = snake((255,0,0),(10,10))
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
WHITE = (255,255,255)

def drawGrid():
    MARGIN = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + MARGIN
        y = y + MARGIN

        pygame.draw.line(surface, (255,255,255), (x,0),(x,w))
        pygame.draw.line(surface, (255,255,255), (0,y),(w,y))


def snake():
    pass #code the snake here






while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        else:
            surface.fill((0, 0, 0))  # Fills the screen with black
            drawGrid()  # Will draw our grid lines
            pygame.display.update()



