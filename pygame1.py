import pygame
import random
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load('Circle.png').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -2)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 2)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-2, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(2, 0)
            
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 1280:
            self.rect.right = 1280
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 1024:
            self.rect.bottom = 1024

class Opponent(pygame.sprite.Sprite):
    def __init__(self):
        super(Opponent, self).__init__()
        self.image = pygame.image.load('triangle.png').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(center=(1500, random.randint(0, 1024)))
        self.speed = random.randint(0, 2)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
            
class Square(pygame.sprite.Sprite):
    def __init__(self):
        super(Square, self).__init__()
        self.image = pygame.image.load('square.png').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(center=(1500, random.randint(0, 1024)))
        self.speed = random.randint(5, 8)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

             
pygame.init()
screen = pygame.display.set_mode((1280, 1024))
player = Player()
background = pygame.Surface(screen.get_size())
background.fill((18, 214, 159))
players = pygame.sprite.Group()
opponents = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
ADDOPPONENT = pygame.USEREVENT + 1
ADDSQUARE = pygame.USEREVENT + 2
pygame.time.set_timer(ADDOPPONENT, 600)
pygame.time.set_timer(ADDSQUARE,1000)
#surf = pygame.Surface((75, 75))
#surf.fill((255, 255, 255))
#rect = surf.get_rect()

running = True
clock = pygame.time.Clock()
fps = 1000
while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif(event.type == ADDOPPONENT):
            new_opponent = Opponent()
            opponents.add(new_opponent)
            all_sprites.add(new_opponent)
        elif(event.type == ADDSQUARE):
            new_square = Square()
            opponents.add(new_square)
            all_sprites.add(new_square)
    screen.blit(background, (0, 0))
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    opponents.update()
    
    
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
    if pygame.sprite.spritecollideany(player, opponents):
        player.kill()
    pygame.display.flip()



pygame.quit()

