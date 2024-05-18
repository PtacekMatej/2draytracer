import pygame as pg
from handleEvents import *
from constants import *
from renderer import render
from rayTracer import traceRay


def main():
    pg.init()

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pg.RESIZABLE)
    pg.display.set_caption('Ray Trecer 2D')

    clock = pg.time.Clock()
    fps = pg.time.Clock()

    PLAYER_ANGLE = 2*PI/3
    PLAYER_POS = [128, 128]

    font = pg.font.Font('freesansbold.ttf', 16)

    cntr = 100
    text = font.render(str(int(100000/fps.tick())) + " fps", True, (255, 255, 255))
    textRect = text.get_rect()


    pg.mouse.set_visible(False)

    while True:
        cntr = (1+cntr)%100
        handleEvents(screen)
        screen.fill((0, 0, 0))
        render(PLAYER_POS, PLAYER_ANGLE, screen)
        PLAYER_POS, PLAYER_ANGLE = handleMovement(PLAYER_POS, PLAYER_ANGLE, clock)


    
        if cntr == 0:
            text = font.render(str(int(100000/fps.tick())) + " fps", True, (255, 255, 255))
            textRect = text.get_rect()
        screen.blit(text, textRect)

        pg.display.flip()


main()