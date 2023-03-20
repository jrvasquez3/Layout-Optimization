import pygame
import time
from tools import *
import math

LAYOUT = pygame.image.load("images/bg.png")
ST_FORKLIFT = pygame.image.load("images/forklift.png")
COIL = pygame.image.load("images/coil.png")
EMPTY = pygame.image.load("images/empty.png")

WIDTH, HEIGHT = LAYOUT.get_width(), LAYOUT.get_height()
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Layout optimization")
FPS = 60


layout_map = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
           ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
           ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
           ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
           ['0','0','0','0','0','0','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
           ['1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','0','0','0','0','0','0','0','0','0'],
           ['2','2','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','2','2','0','0','0','1','1','1','1','1','0'],
           ['2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','0','0','0','2','2','2','2','2','0'],
           ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','2','0','0'],
           ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','0','0','0'],
           ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','0','0','0'],
           ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
           ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']]


class Forklift:
    IMG = ST_FORKLIFT
    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.START_POS
        self.acceleration = 0.1
    
    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel
    
    def draw(self, win):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)

    def move_foward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()
    
    def move_backward(self):
        self.vel = max(self.vel - self.acceleration, -self.max_vel/2)
        self.move()
    
    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel
        self.y -= vertical
        self.x -= horizontal

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()




def draw(win, images, forklift):
    for img, pos in images:
        win.blit(img, pos)
    
    forklift.draw(win)
    pygame.display.update()


class Test_Forklift(Forklift):
    IMG = ST_FORKLIFT
    START_POS = (150, 200)


def move_player_forklift(fork_lift):
    keys = pygame.key.get_pressed()
    moved = False
    if keys[pygame.K_LEFT]:
        fork_lift.rotate(left=True)
    if keys[pygame.K_RIGHT]:
        fork_lift.rotate(right=True)
    if keys[pygame.K_UP]:
        moved = True
        fork_lift.move_foward()
    if keys[pygame.K_DOWN]:
        fork_lift.move_backward()
        moved = True
    if not moved:
        fork_lift.reduce_speed()


run = True
clock = pygame.time.Clock()
images = [(LAYOUT, (0,0)), 
        (COIL, (550, 5)),  (COIL, (640, 5)),  (COIL, (730, 5)),      (COIL, (820, 5)),   (COIL, (910, 5)),    (COIL, (1000, 5)),
        (EMPTY, (550, 87)),(EMPTY, (640, 87)),(COIL, (730, 87)),     (COIL, (820, 87)),  (COIL, (910, 87)),   (COIL, (1000, 87)),
                                              ((EMPTY, (730, 209))), (COIL, (820, 209)), (COIL, (910, 209)), (COIL, (1000, 209)) ]
fork_lift = Test_Forklift(4, 4)
while run:


    clock.tick(FPS)
    draw(WIN, images, fork_lift)
    #WIN.blit(LAYOUT, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    move_player_forklift(fork_lift=fork_lift)




    
pygame.quit()