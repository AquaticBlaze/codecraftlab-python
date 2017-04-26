import pygame
from pygame.locals import *

class Land(pygame.sprite.Sprite):
    def __init__(self):
        super(Land, self).__init__()
        self.surf = pygame.Surface((20, 20))
        self.surf.fill((55, 126, 48))
        self.rect = self.surf.get_rect()

pygame.init()
screen = pygame.display.set_mode((700, 700))
land = Land()      
tr = 0
c = 0
r = 0
t = 0
while tr < 1225:
    screen.blit(land.surf, (1 + r, 1 + c))
    pygame.display.flip()
    tr = tr + 1
    r = r + 20
    t = t + 1
    if t == 36:
        r = r + 20
        tr = 0
        c = 0
        

