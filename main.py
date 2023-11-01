import pygame as pg
from config import *
from CityGrid import CityGrid

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode(WINDOW_SIZE)
screen.fill(BACKGROUND)


city_grid = CityGrid(screen, CELL_QTY_X, CELL_QTY_Y, CELL_SIZE, NUMS_BANNED_CELL)
city_grid.draw()
# city_grid.draw_towers()
# print(city_grid.percentage_coverage)
pg.display.update()

while IS_RUN:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            IS_RUN = False

    clock.tick(FPS)
