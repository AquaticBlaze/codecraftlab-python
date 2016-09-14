import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1280, 1024))

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False





pygame.quit()

