import pygame as pg

from Logic import Logic
from config import *
from CityGrid import CityGrid

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode(WINDOW_SIZE)
screen.fill(BACKGROUND)


logic = Logic(CELL_QTY_X, CELL_QTY_Y, 0)
city_grid = CityGrid(screen)
logic.make_best_move()
city_grid.draw(logic.field)
pg.display.update()

logic.make_best_move()
city_grid.draw(logic.field)
pg.display.update()


while IS_RUN:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            IS_RUN = False

    clock.tick(FPS)
