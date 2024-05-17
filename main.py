import pygame as pg


def main():
    pg.init()
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption('demo')


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()


main()