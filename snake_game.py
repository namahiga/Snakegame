import random
import sys
import pygame
from pygame.locals import *
pygame.init() #initializing pygame
pygame.display.set_caption("snake game")
#Global Variables
rows = 16
width = 500
height = 500
w = 500
MARGIN = 0
surface = pygame.display.set_mode((500, 500))
#snake = Player((255,0,0),(16,16))
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





class Player(pygame.sprite.Sprite):
    def __init__(self,col,pos):
        super(Player, self).__init__()
        self.surf = pygame.Surface(pos)
        self.surf.fill(col)
        self.rect = self.surf.get_rect()
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)



while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        else:
            
            surface.fill((0, 0, 0))  # Fills the screen with black
            drawGrid()  # Will draw our grid lines
            pygame.display.update()
            




