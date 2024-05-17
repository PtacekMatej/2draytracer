import pygame as pg
from math import *
from handleEvents import handleMovement
from constants import *
from utils import *
from rayTracer import traceRayHorizontal, traceRayVertical




def render(pos, angle, screen):
    scr_width, scr_height = pg.display.get_surface().get_size()
    for i in range(-scr_width//2, scr_width//2):
        angle_diff = i * PI / scr_width / 3
        new_angle = angle + angle_diff
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

        shade /=  max(1, d / 10 / GRID_SIZE)
        color = (0, int(shade), 0)
        height = scr_height
        if d != 0:
            height = int(scr_width * BLOCK_SIZE / (d * cos(angle_diff) ))

        pg.draw.rect(screen, color, pg.Rect(scr_width - (i+scr_width//2), (scr_height-height)/2, 1, height))