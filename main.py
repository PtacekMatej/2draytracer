import pygame as pg
from handleEvents import *
from constants import *
from renderer import render
from rayTracer import traceRay









def main():
    pg.init()
    font = pg.font.Font('freesansbold.ttf', 32)

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pg.RESIZABLE)
    pg.display.set_caption('demo')

    clock = pg.time.Clock()

    PLAYER_ANGLE = 2*PI/3
    PLAYER_POS = [128, 128]


    pg.mouse.set_visible(False)

    while True:
        handleEvents(screen)
        screen.fill((0, 0, 0))
        render(PLAYER_POS, PLAYER_ANGLE, screen)
        PLAYER_POS, PLAYER_ANGLE = handleMovement(PLAYER_POS, PLAYER_ANGLE, clock)
        pg.display.flip()


main()