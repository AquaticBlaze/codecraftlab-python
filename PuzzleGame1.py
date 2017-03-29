import pygame
from pygame import *
pygame.init()

screen = pygame.display.set_mode((750, 540))
background = pygame.Surface(screen.get_size())
background.fill((0, 0, 0))

run = True
while run:

    for event in pygame.event.get():
        
        if event.type == QUIT:
            run = False
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            run = False
        
pygame.quit()            

    







