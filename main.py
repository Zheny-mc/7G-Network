import pygame as pg

from Logic import Logic
from config import *
from CityGrid import CityGrid

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode(WINDOW_SIZE)
screen.fill(BACKGROUND)

logic = Logic(CELL_QTY_X, CELL_QTY_Y, RADIUS, NUMS_BANNED_CELL)
city_grid = CityGrid(screen)

while IS_RUN:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            IS_RUN = False

    logic.optimize_towers()
    city_grid.draw(logic.field)
    pg.display.update()
    clock.tick(FPS)
