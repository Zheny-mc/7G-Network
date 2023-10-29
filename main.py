import pygame as pg

FPS = 10
WINDOW_SIZE = (640, 480)
BACKGROUND = (150, 90, 30)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
IS_RUN = True

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode(WINDOW_SIZE)
screen.fill(BACKGROUND)


while IS_RUN:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            IS_RUN = False
    pg.display.update()
    clock.tick(FPS)



