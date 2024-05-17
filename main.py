import pygame as pg
from math import *


PI = 3.14159265358979323



BLOCK_SIZE = 16
GRID_SIZE = 8


PLAYER_POS = [64, 64]

GAME_WORLD = [
    1, 1, 1, 1, 1, 1, 1, 1,
    1, 0, 0, 1, 0, 0, 0, 1, 
    1, 0, 0, 1, 0, 1, 0, 1, 
    1, 1, 0, 0, 0, 0, 0, 1, 
    1, 0, 0, 0, 0, 0, 0, 1, 
    1, 0, 0, 0, 0, 1, 0, 1, 
    1, 0, 1, 0, 0, 0, 0, 1, 
    1, 1, 1, 1, 1, 1, 1, 1
]

def cot(x):
    return 1/tan(x)


def traceRayHorizontal(pos_x, pos_y, angle):
    dirX = 1
    idx_correctionX = 0
    if angle < PI:
        dirX = -1
        idx_correctionX = -1
    dist = pos_x % BLOCK_SIZE
    if dirX == -1:
        dist -= BLOCK_SIZE

    y_diff = BLOCK_SIZE * cot(angle) * dirX
    y = pos_y + dist * cot(angle)
    x = pos_x + dist

    for _ in range(10):
        idx_x = (x // BLOCK_SIZE) + idx_correctionX
        idx_y = (y // BLOCK_SIZE)
        if idx_x < 0 or idx_y < 0 or idx_x >= GRID_SIZE or idx_y >= GRID_SIZE:
            return (float('inf'), float('inf'))
        block = int(idx_x + idx_y * GRID_SIZE)
        if(GAME_WORLD[block] > 0):
            return (x, y)
        y += y_diff
        x += BLOCK_SIZE * dirX

def traceRayVertical(pos_x, pos_y, angle):
    dirY = 1
    idx_correctionY = 0
    if angle < PI / 2 or angle > 3*PI/2:
        dirY = -1
        idx_correctionY = -1
    
    dist = pos_y % BLOCK_SIZE
    if dirY == -1:
        dist -= BLOCK_SIZE
    
    x_diff = BLOCK_SIZE * tan(angle) * dirY
    x = pos_x + dist * tan(angle)
    y = pos_y + dist
    for _ in range(10):
        idx_x = (x // BLOCK_SIZE)
        idx_y = (y // BLOCK_SIZE) + idx_correctionY
        if idx_x < 0 or idx_y < 0 or idx_x >= GRID_SIZE or idx_y >= GRID_SIZE:
            return (float('inf'), float('inf'))
        block = int(idx_x + idx_y * GRID_SIZE)
        if(GAME_WORLD[block] > 0):
            return (x, y)
        y += BLOCK_SIZE * dirY
        x += x_diff

    
    
        
def dist(a, b):
    x = a[0] - b[0]
    y = a[1] - b[1]
    return sqrt(x * x + y * y)

        

def traceRay(pos, angle):
    pos_h = traceRayHorizontal(pos[0], pos[1], angle)
    pos_v = traceRayVertical(pos[0], pos[1], angle)
    h = dist(pos, pos_h)
    v = dist(pos, pos_v)
    if h < v:
        return pos_h
    return pos_v







def main():
    pg.init()
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    font = pg.font.Font('freesansbold.ttf', 32)

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption('demo')

    clock = pg.time.Clock()

    PLAYER_ANGLE = 2*PI/3
    while True:
        screen.fill((0, 0, 0))
        PLAYER_ANGLE = PLAYER_ANGLE + 0.001 * clock.tick()
        if PLAYER_ANGLE > 2*PI:
            PLAYER_ANGLE -= 2*PI

        for block_idx in range(len(GAME_WORLD)):
            if GAME_WORLD[block_idx] == 1:
                pg.draw.rect(screen, (255, 255, 255), pg.Rect(BLOCK_SIZE * (block_idx % 8), BLOCK_SIZE * (block_idx // 8), BLOCK_SIZE, BLOCK_SIZE))

        hit = traceRay(PLAYER_POS, PLAYER_ANGLE)
        pg.draw.line(screen, (0, 255, 0), (PLAYER_POS[0], PLAYER_POS[1]), hit)
        

        pg.draw.rect(screen, (255, 0, 0), pg.Rect(PLAYER_POS[0] - 1, PLAYER_POS[1] - 1, 3, 3))


        

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        pg.display.flip()


main()