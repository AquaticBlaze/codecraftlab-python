#import pygame
import pygame
from pygame import *

#create window
WIN_WIDTH = 1000
WIN_HEIGHT = 640
HALF_WIDTH = int(WIN_WIDTH / 2)
HALF_HEIGHT = int(WIN_HEIGHT / 2)

DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
DEPTH = 32
FLAGS = 0
CAMERA_SLACK = 30

# main loop
def main():
    global cameraX, cameraY
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("Platformer")
    timer = pygame.time.Clock()

    up = down = left = right = running = False
    bg = Surface((32,32))
    bg.convert()
    bg.fill(Color(0, 183, 198))
    entities = pygame.sprite.Group()
    player = Player(32, 32)
    platforms = []
    run = True

    #create level
    x = y = 0
    level = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPXXPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPXPPPPPPP",
        "P                                                                                                                                                              PPPPPPPP                 BG                PP                                                                                                                                                                  N                                                                                                      LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL                             NPPPPPPPPPPPPPP                                           P                               PP                                                                                         P",
        "P                                                                                                                                                              PPPPPPPP                 BG                PP                                                                                         L                                                                        N                                                                                                       LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL                              NPPPPPPPPPPPPPP                                           P                               PP                                                                                        EP",
        "P                                                                                                                                                              PPPPPPPP                 BG                PP                                                                                                                                                                  N                                                      LL                                                LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL    L                          NPPPPPPPPPPPPPP      PPPPPPPPPPPPPPPPPPPPPPP     PPPPPPPPPP         PPPPPPPPPPPPPPPPPPPP  PP     PPPPPPPPPPPXPPPPPPPPPPPPPPPPPPPPPPPPPPPPPXPPPPPPPPPPPXPPPPPPPPPPXXXPPPPPPPPPPPPPPPPPP",
        "P                                    PPP                                                                                                                       PPPPPPPP                 BG                PP                                                                                                                                                                  N                                                      LL                                     LL          LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL                  L             N                                 P                       P                            P  PP                   P                                                        N           P",
        "P                                    PPP                                                                                                                       PPPPPPPP          PPGGGGGBG                PP                                                                                                              L                               L                   N                                                                                             LL           LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL                                 N                                 P                       P                            P  PP                   P                                                        N           P",
        "P                                    PPP     PPPP                                                                              `                               PPPPPPPP          PP    GBG                PP                                                                                                                                                                  N                                                                                LL                         LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL                                  N                                 P                       PPP                          P  PPP                  P   PPP                                                  N           P",
        "P                                    PPP                                                                                                                       PPPPPPPP           P    GBG                PP                                                                                                                                                                  N                                                                                LL                          LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL                                   N                  P              P                       P                         XX P  PF                   X   P                                                    N           P",
        "P                                    PPP                                                                                                                       PPPPPPPP          PPGGGGGBG       G        PP                                                                                                                                 L                                N                                                                                                             LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL                           L        N                                 P     L                 P                            P  PF                   P   P           PXP     XPP                              N           P",
        "P                          PPPPPPP   PPP                                                                                                                       PPPPPPPP          PPBBBBBBG       G        PP                                                                                                                                                                  N                                                                                                              LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL                                     N                                 P                       P       PP                   P  PF                   P   P                                                    N           P",
        "P                                    PPP                                                                                                                       PPPPPPPP          PPBGGGGGG       G        PP                                                                                          L                                                                       N                                                                                              LL                                      LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL             L                        N                                 P                       P                PP          P  PPP                  P   P                          PPP                       N           P",
        "P                                    PPP                                                                                                                       PPPPPPPP          PPBGGGBBB       G        PP                                                                                                                                                                  N                                                             LL                               LL                                       LLLLLLLLLLLLLLLL         LLLLLLLLLLLLLLL                                       N        PP                       P                       P                            P  PP          P        P   P     X               X                              N N         P",
        "P                                    PPP                      PPPP                                                                                             PPPPPPP           PPBBBBBGG       G        PP                   BBB                                                                                            L                                               N                                                             LL                                                                         LLLLLLLLLLLLLL           LLLLLLLLLLLLL                            L           N                                 P           L           P                         PP P  PX          X            P                X              P                    N N         P",
        "P         PPPPPPP                    PPP                                                                                                                       PPPPPPPP          PPGGGGGG        G        PP                  BB BB       G                                                                                                                                   N                                                                                                                                         LLLLLLLLLLLL             LLLLLLLLLLL                                         N                   PP            P                       P              XX            P  PP          X            X                               X                      N         P",
        "P                                    PPP                            PPPPPPPPPP            PPPPPPPPPP                                                           PPPPPPPP          PP              G        PP                 BB   BB      G                                                                                                                                   N                                                                                                              LLLLLLLLLLLLLLLLLLLL        LLLLLLLLLL               LLLLLLLLL                                          N                                 P                       P                            P  PPPPPXXXPPPXPPPPPPPPPPPPPPFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFPPPPPPPXPPPPPPPPPPPPPPPPPPPP      P",  
        "P                                    PPP                            PPPPPPPPPP            PPPPPPPPPP                   P                                       PPPPPPPP          PP              G        PP           BBB  BB     BB  BBBG                                                                       L                                    L                      N                                                                                                             LLLLLLLLLLLLLLLLLLLLLL                                                                                   N                              PP P   L                   P                            P  PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP    P",  
        "P                                    PPP                            PPPPPPPPPP            PPPPPPPPPP                   PLLLLLLLLP   PLLLLLLLLLPPPPLLLLLLLL    LLLLLLLLP          PP           BBBG        PP       BBBBB BBBB       BBBB  G                                                                                                                                   N                                                                          LL                                LLLLLLLLLLLLLLLLLLLLLLLL                      LLL                                                         N                                 P                       P    XX               PP     P  P                                  P                                                      P",
        "P                                    PPP                            PPPPPPPPPPLLLLLLLLLLLLPPPPPPPPPP                   PLLLLLLLLP   PLLLLLLLLLLLLPLLLLLLLL    LLLLLLLLP           P           GGGG        PPGGGGGGGGGGG   GGGGGGGGGGGG    G                                                                                                                                   N                                                                          LL                               LLLLLLLLLLLLLLLLLLLLLLLLLL                    LLLLL                                L                       N                                 P                       P                            P  P                                  P                                                      P",
        "P                 PPPPPPPPPPP        PPP                            PPPPPPPPPPLLLLLLLLLLLLPPPPPPPPPP       PPPP        PLLLLLLLLP   PLLLLLLLLLLLLPLLL         LLLLLLLLP          PP                       PP         GG   GG         G    G                                                                                                                                   N                                  FF                                                                      LLLLLLLLLLLLLLLLLLLLLLLLLLLL                  LLLLLLL                                                       N                                 P                  L    P                            P  P                                  P                                                      P",
        "P                                    PPP                            PPPPPPPPPPLLLLLLLLLLLLPPPPPPPPPP                   PLLLLLLLLPPPPPLLLLLLLLLLLLPLLLP PPPPPPPLLLLLLLLP          PP     BBB               PP         GGGGGGG         GGGGGG                                                                                       L                L                          N                          P       PP                                                                     LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL                                          N                    PP           P                       P                 PP         P  P                                  P            PPPP       PPPP       XXXX               PP",
        "P                                    PPP                            PPPPPPPPPPLLLLLLLLLLLLPPPPPPPPPP                   PLLLLLLLLLLLLLLLLLLLLLLLLLPLLLL LLLLLLLLLLLLLLLP          PP     GGG               PP         GG   GG         GG                                                                   L                                                                   N                   P      P       PP               LL                                       LL          LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL      L                      L           N                                 P                       P                            P  P             P       PPPPPP                                                              P",
        "P                                    PPP                            PPPPPPPPPPLLLLLLLLLLLLPPPPPPPPPP                   PLLLLLLLLLLLLLLLLLLLLLLLLLPLLLL LLLLLLLLLLLLLLLP          PP                       PP            G               GG                                                                                                                                  N N             P     P      P       PP               LL                                       LL         LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL                                      N N          PP                     P    L                                               P                P       PPPPPP                                                              P",
        "P                                    PPP                            PPPPPPPPPPLLLLLLLLLLLLPPPPPPPPPP                   PLLLLLLLLLLLLLLLLLLLLLLLLLPLLLL                           PP          GGGG                 PPPGGGGGGGGLLLLLLLGGGGGG                                                                                                                                  N          P    P     P      P       PP                                                                  LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL                                     N                                   P                                                    P                P       PPPPPP                                                              P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPLLLLLLLLLLLLLLLLLLLLLLLLLLLLPPPPPPPPPPLLLLLLLLLLLLPPPPPPPPPPLLLLLLLLLLLLLLLLLLLPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPLLLLLLLLLLLLLLLLLLLLPPPPPPPPPPPPPP                     PPPPPPPPPPPPPPPPPPFFFFPPPPPPPPPPPLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLPPPPPPPPPPPPLLLLPLLLLLPLLLLLLPLLLLLLLPPLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLPPPPPPPPLLLLLLLLLLLLLLLLLLLLLLLLLLLLPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPXPPPPPPPPXXPPPPPPPPPPPPPPPPPPPPPPPLLLLLLLPPPPPPPPPPPPPPPPPPPPPPPPPPXXXXXXXXXXXXXXXPPPPPPPPPPPPPPPPPPPPPPPPPPPP"]

    #create blocks    
    for row in level:
        for col in row:
            if col == "P":
                p = Platform(x, y)
                platforms.append(p)
                entities.add(p)
            if col == "E":
                e = ExitBlock(x, y)
                platforms.append(e)
                entities.add(e)
            if col == "L":
                l = Lava(x, y)
                platforms.append(l)
                entities.add(l)
            if col == "G":
                g = Ghost(x, y)
                platforms.append(g)
                entities.add(g)
            if col == "B":
                b = Background(x, y)
                entities.add(b)
            if col == "F":
                f = Flyportal(x, y)
                platforms.append(f)
                entities.add(f)
            if col == "N":
                n = Normalportal(x, y)
                platforms.append(n)
                entities.add(n)
            if col == "X":
                X = Poison(x, y)
                platforms.append(X)
                entities.add(X)
                
            x += 32
        y += 32
        x = 0

    #set level size
    total_level_width  = len(level[0])*100
    total_level_height = len(level)*32
    camera = Camera(complex_camera, total_level_width, total_level_height)
    entities.add(player)

    #detect keys
    while run:
        timer.tick(60)

        for e in pygame.event.get():
        
            if e.type == QUIT:
                run = False
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                run = False
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_DOWN:
                down = True
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYDOWN and e.key == K_SPACE:
                running = True
                    
            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_DOWN:
                   down = False
            if e.type == KEYUP and e.key == K_RIGHT:
                 right = False
            if e.type == KEYUP and e.key == K_LEFT:
                 left = False
            
                

        for y in range(32):
            for x in range(32):
                screen.blit(bg, (x * 32, y * 32))
        
        camera.update(player)

        player.update(up, down, left, right, running, platforms)
        for e in entities:
            screen.blit(e.image, camera.apply(e))

        pygame.display.update()

    pygame.quit()

#define camera
class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

def simple_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    return Rect(-l+HALF_WIDTH, -t+HALF_HEIGHT, w, h)

def complex_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l+HALF_WIDTH, -t+HALF_HEIGHT, w, h

    l = min(0, l)
    l = max(-(camera.width-WIN_WIDTH), l)   
    t = max(-(camera.height-WIN_HEIGHT), t) 
    t = min(0, t)                           
    return Rect(l, t, w, h)

#define entities
class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class Player(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.mode = 0
        self.dir = 0
        self.onGround = False
        self.image = Surface((32,32))
        self.image.fill(Color("#0000FF"))
        self.image.convert()
        self.rect = Rect(x, y, 32, 32)

    #create gravity and movement
    def update(self, up, down, left, right, running, platforms):
        if self.mode == 0:    
            if up:
                
                if self.onGround: self.yvel -= 10
            if down:
                pass
            if running:
                self.xvel = 12
            if left:
                self.xvel = -8
            if right:
                self.xvel = 8
            if not self.onGround:
                self.yvel += 0.3
            if self.yvel > 100: self.yvel = 100
            
        if self.mode == 1:
            if up:
                self.yvel = -8
                self.dir = 1
            if down:
                self.yvel = 8
                self.dir = 0
            if not (up or down):
                if self.dir == 0:
                    if self.yvel == 0:
                        self.yvel = 0
                    else:
                        self.yvel = self.yvel - 0.5
                else:
                    if self.yvel == 0:
                        self.yvel = 0
                    else:
                        self.yvel = self.yvel + 0.5
            
        if not(left or right):
            if self.mode == 0:
                self.xvel = 0
            if self.mode == 1:
                self.xvel = 8
            
       
        self.rect.left += self.xvel
       
        self.collide(self.xvel, 0, platforms)

        self.rect.top += self.yvel
        
        self.onGround = False;
        
        self.collide(0, self.yvel, platforms)

    #detect collisions
    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, ExitBlock):
                    pygame.event.post(pygame.event.Event(QUIT))
                if isinstance(p, Lava):
                    self.kill()
                    pygame.event.post(pygame.event.Event(QUIT))
                if isinstance(p, Poison):
                    self.kill()
                    pygame.event.post(pygame.event.Event(QUIT))
                if isinstance(p, Flyportal):
                    self.mode = 1
                if isinstance(p, Normalportal):
                    self.mode = 0
                if xvel > 0:
                    self.rect.right = p.rect.left
                if xvel < 0:
                    self.rect.left = p.rect.right
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    if self.mode == 0:
                        self.onGround = True
                        self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom
            

#define blocks
class Platform(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = Surface((32, 32))
        self.image.convert()
        self.image.fill(Color(0, 128, 0))
        self.rect = Rect(x, y, 32, 32)

    def update(self):
        pass

class ExitBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(Color(255 ,255 , 255))

class Lava(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = Surface((32, 32))
        self.image.convert()
        self.image.fill(Color(128, 0, 0))
        self.rect = Rect(x, y, 32, 32)    

class Ghost(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = Surface((32, 32))
        self.image.convert()
        self.image.fill(Color(0, 183, 198))
        self.rect = Rect(x, y, 32, 32)    

    def update(self):
        pass

class Background(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = Surface((32, 32))
        self.image.convert()
        self.image.fill(Color(254, 242, 175))
        self.rect = Rect(x, y, 32, 32)

class Flyportal(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = Surface((32, 32))
        self.image.convert()
        self.image.fill(Color(255, 255, 0))
        self.rect = Rect(x, y, 32, 32)

class Normalportal(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = Surface((32, 32))
        self.image.convert()
        self.image.fill(Color(143, 217, 234))
        self.rect = Rect(x, y, 32, 32)

class Poison(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = Surface((32, 32))
        self.image.convert()
        self.image.fill(Color(62, 132, 60))
        self.rect = Rect(x, y, 32, 32)

#run program        
if __name__ == "__main__":
    main()
