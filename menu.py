import pygame as pg

def handleMenu(screen):
    pg.mouse.set_visible(True)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    pg.mouse.set_visible(False)
                    pg.mouse.get_rel()
                    return
        w, h = pg.display.get_surface().get_size()
        pg.draw.rect(screen, (255, 255, 255), pg.Rect(w//10, h//10, w-w//5, h-h//5))
        pg.display.flip()