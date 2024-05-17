import pygame as pg
from handleEvents import handleMovement
from constants import *
from renderer import render
from rayTracer import traceRay









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