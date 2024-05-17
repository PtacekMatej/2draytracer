import pygame as pg
from math import *
from handleEvents import handleMovement
from constants import *
from utils import *
from rayTracer import traceRayHorizontal, traceRayVertical




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