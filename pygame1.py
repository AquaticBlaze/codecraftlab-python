import pygame
import random
import time
import urllib2,json
from pprint import pprint
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
        self.speed = random.randint(15, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

class Pentagon(pygame.sprite.Sprite):
    def __init__(self, rect):
        super(Pentagon, self).__init__()
        self.image = pygame.image.load('Pentagon.png').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(center=(1500, rect.top))
        self.speed = random.randint(5, 6)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

class Hexagon(pygame.sprite.Sprite):
    def __init__(self):
        super(Hexagon, self).__init__()
        self.images = []
        self.images.append(pygame.image.load('Hexagon.png'))
        self.images.append(pygame.image.load('Hexagon2.png'))
        self.index = 0
        self.image = self.images[self.index]
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(center=(1500, random.randint(0, 1024)))
        self.speed = random.randint(1, 2)
        self.last = pygame.time.get_ticks()
        self.image = self.images[self.index]
        self.cooldown = 1000
    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        now = pygame.time.get_ticks()
        if now - self.last >= self.cooldown:
            self.image = self.images[self.index]
            self.image.set_colorkey((255, 255, 255), RLEACCEL)
            self.last = now
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

def getWeatherCondition(station_data):
    cond = str(station_data[0]['station']['condition'])
    return cond


url = 'https://brevard.weatherstem.com/api'
indata = {'api_key':'x023yuaj','stations':['pac']}
request = urllib2.Request(url)
request.add_header('Contest-Type','application/json')
outdata = json.dumps(indata)
response = urllib2.urlopen(request,outdata)
station_data = json.load(response)
print(getWeatherCondition(station_data))
pygame.init()
my_font = pygame.font.SysFont("times", 20)
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
ADDPENTAGON = pygame.USEREVENT + 3
ADDHEXAGON = pygame.USEREVENT + 4
pygame.time.set_timer(ADDOPPONENT, 600)
pygame.time.set_timer(ADDSQUARE,10000)
pygame.time.set_timer(ADDPENTAGON,3000)
pygame.time.set_timer(ADDHEXAGON,3000)
#surf = pygame.Surface((75, 75))
#surf.fill((255, 255, 255))
#rect = surf.get_rect()

running = True
clock = pygame.time.Clock()
fps = 1000
playerkill = False
gamestart = False
start_ticks = 0
lives = 10
print 'Press space to start!'
while running:
    clock.tick(fps)
    if not gamestart:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    gamestart = True
                    start_ticks = pygame.time.get_ticks()
                    break
        continue
    seconds = (pygame.time.get_ticks()-start_ticks)/1000
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
        elif(event.type == ADDPENTAGON):
            new_pentagon = Pentagon(player.rect)
            opponents.add(new_pentagon)
            all_sprites.add(new_pentagon)
        elif(event.type == ADDHEXAGON):
            new_hexagon = Hexagon()
            opponents.add(new_hexagon)
            all_sprites.add(new_hexagon)
    screen.blit(background, (0, 0))
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    opponents.update()

    if not lives == 0:    
        timetext = my_font.render("Time = " + str(seconds), 1, (0, 0, 0))
        lifetext = my_font.render("Lives = " + str(lives), 1, (0, 0, 0))
    screen.blit(timetext, (5, 10))
    screen.blit(lifetext, (5, 30))
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    spr = pygame.sprite.spritecollideany(player, opponents)
    if not playerkill and spr:
        spr.kill()
        lives = lives-1
        if lives == 0:
            playerkill = True
            player.kill()
            print ('You survived ' + str(seconds) + ' seconds!')
    pygame.display.flip()


pygame.quit()

