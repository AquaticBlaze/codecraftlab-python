import pygame
from pygame import *
pygame.init()

class P1(pygame.sprite.Sprite):
    def __init__(self):
        super(P1, self).__init__()
        self.image = pygame.image.load('P1.png').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(center=(375, 270))

class P2(pygame.sprite.Sprite):
    def __init__(self):
        super(P1, self).__init__()
        self.image = pygame.image.load('P2.png').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(center=(375, 270))

puzzle = 1
screen = pygame.display.set_mode((750, 540))
background = pygame.Surface(screen.get_size())
background.fill((60, 57, 21))        
p1 = P1()
p2 = P2()
all_sprites = pygame.sprite.Group()
all_sprites.add(p1)

run = True
while run:
    screen.blit(background, (0, 0))
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
    pygame.display.flip()

    for event in pygame.event.get():
        
        if event.type == QUIT:
            run = False
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            run = False

    if puzzle == 1:
            print('What is the answer?')
            answer = raw_input()
            if answer == "61013":
                puzzle = 2
                p1.kill()
                all_sprites.add(p2)
    if puzzle == 2:
        print('What is the answer?')
            answer = raw_input()
            if answer == "mops":
                puzzle = 3
                p2.kill()
                #all_sprites.add(p3)
        
                


pygame.quit()            

    







