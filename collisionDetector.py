from constants import *

def isInWall(pos):
    x, y = pos
    x //= BLOCK_SIZE 
    y //= BLOCK_SIZE
    if x < 0 or y < 0 or x >= GRID_SIZE or y >= GRID_SIZE:
        return True
    return GAME_WORLD[int(x + GRID_SIZE * y)] == 1
