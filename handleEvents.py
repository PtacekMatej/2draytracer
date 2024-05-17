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

    if keys[pg.K_w]:
        x -= sin(angle) * SPEED_M * delta_t
        y -= cos(angle) * SPEED_M * delta_t
    if keys[pg.K_s]:
        x += sin(angle) * SPEED_M * delta_t
        y += cos(angle) * SPEED_M * delta_t
    if keys[pg.K_a]:
        x -= cos(angle) * SPEED_M * delta_t
        y += sin(angle) * SPEED_M * delta_t
    if keys[pg.K_d]:
        x += cos(angle) * SPEED_M * delta_t
        y -= sin(angle) * SPEED_M * delta_t

        
    
    return ((x, y), angle)

