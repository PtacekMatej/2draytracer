import pygame as pg
from math import *
from handleEvents import handleMovement
from constants import *
from utils import *


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

        

def traceRay(pos, angle):
    pos_h = traceRayHorizontal(pos[0], pos[1], angle)
    pos_v = traceRayVertical(pos[0], pos[1], angle)
    h = dist(pos, pos_h)
    v = dist(pos, pos_v)
    if h < v:
        return pos_h
    return pos_v