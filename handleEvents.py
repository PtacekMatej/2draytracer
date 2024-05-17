import pygame as pg
from constants import *
from math import *
from menu import handleMenu


def handleEvents(screen):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                handleMenu(screen)


def handleMovement(pos, angle, clock):
    keys = pg.key.get_pressed()
    delta_t = clock.tick()
    rotation, _ = pg.mouse.get_rel()
    pg.mouse.set_pos((SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
    angle -= SPEED_R * delta_t * rotation
    if angle < 0:
        angle += 2*PI
    elif angle > 2*PI:
        angle -= 2*PI

    x, y = pos

    pos_diff = [0, 0]

    if keys[pg.K_w]:
        pos_diff[0] -= sin(angle)
        pos_diff[1] -= cos(angle)
    if keys[pg.K_s]:
        pos_diff[0] += sin(angle)
        pos_diff[1] += cos(angle)
    if keys[pg.K_a]:
        pos_diff[0] -= cos(angle)
        pos_diff[1] += sin(angle)
    if keys[pg.K_d]:
        pos_diff[0] += cos(angle)
        pos_diff[1] -= sin(angle)

    pos_diff_size = dist([0, 0], pos_diff)

    if pos_diff_size != 0:
        pos_diff[0] /= pos_diff_size
        pos_diff[1] /= pos_diff_size
        
    
    return ((x + pos_diff[0] * delta_t * SPEED_M, y + pos_diff[1] * delta_t * SPEED_M), angle)

