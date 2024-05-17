import pygame as pg
from math import *
from handleEvents import handleMovement
from constants import *

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


def render(pos, angle, screen):
    for i in range(-100, 100):
        new_angle = angle + (i * PI / 600)
        if new_angle < 0:
            new_angle += 2*PI
        elif new_angle > 2*PI:
            new_angle -= 2*PI
        pos_h = traceRayHorizontal(pos[0], pos[1], new_angle)
        pos_v = traceRayVertical(pos[0], pos[1], new_angle)
        h = dist(pos, pos_h)
        v = dist(pos, pos_v)
        d = min(h, v)
        shade = 255
        if(d == h):
            shade = 192

        shade /= max(1, d / 100)
        color = (0, int(shade), 0)
        height = int(8000 / (d * cos(i * PI / 600) ))

        pg.draw.rect(screen, color, pg.Rect((i+100)*4, (SCREEN_HEIGHT-height)/2, 4, height))










def main():
    pg.init()
    font = pg.font.Font('freesansbold.ttf', 32)

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption('demo')

    clock = pg.time.Clock()

    PLAYER_ANGLE = 2*PI/3
    PLAYER_POS = [64, 64]


    pg.mouse.set_visible(False)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()




        screen.fill((0, 0, 0))



        render(PLAYER_POS, PLAYER_ANGLE, screen)


        pg.draw.rect(screen, (0, 0, 0), pg.Rect(0, 0, BLOCK_SIZE * GRID_SIZE, BLOCK_SIZE * GRID_SIZE))
        for block_idx in range(len(GAME_WORLD)):
            if GAME_WORLD[block_idx] == 1:
                pg.draw.rect(screen, (255, 255, 255), pg.Rect(BLOCK_SIZE * (block_idx % 8), BLOCK_SIZE * (block_idx // 8), BLOCK_SIZE, BLOCK_SIZE))


        hit = traceRay(PLAYER_POS, PLAYER_ANGLE)
        pg.draw.line(screen, (0, 255, 0), (PLAYER_POS[0], PLAYER_POS[1]), hit)
        

        pg.draw.rect(screen, (255, 0, 0), pg.Rect(PLAYER_POS[0] - 1, PLAYER_POS[1] - 1, 3, 3))





        PLAYER_POS, PLAYER_ANGLE = handleMovement(PLAYER_POS, PLAYER_ANGLE, clock)
        

        
                
        pg.display.flip()


main()