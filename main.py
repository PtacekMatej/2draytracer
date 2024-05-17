import pygame as pg
from math import *



BLOCK_SIZE = 16
GRID_SIZE = 8

GAME_WORLD = [
    1, 1, 1, 1, 1, 1, 1, 1,
    1, 0, 0, 0, 0, 0, 0, 1, 
    1, 0, 1, 0, 0, 1, 0, 1, 
    1, 0, 0, 0, 0, 0, 0, 1, 
    1, 0, 0, 1, 0, 0, 0, 1, 
    1, 0, 1, 1, 0, 1, 0, 1, 
    1, 0, 0, 0, 0, 1, 0, 1, 
    1, 1, 1, 1, 1, 1, 1, 1
]






def main():
    pg.init()
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption('demo')


    while True:

        for block_idx in range(len(GAME_WORLD)):
            if GAME_WORLD[block_idx] == 1:
                pg.draw.rect(screen, (255, 255, 255), pg.Rect(BLOCK_SIZE * (block_idx % 8), BLOCK_SIZE * (block_idx // 8), BLOCK_SIZE, BLOCK_SIZE))


        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

        pg.display.flip()


main()