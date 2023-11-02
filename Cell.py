import pygame as pg
from config import MARGIN, CELL_SIZE


class Cell:
    def __init__(self, x: int, y: int, size: int=CELL_SIZE) -> None:
        self.__x = x
        self.__y = y
        self.__size = size

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    def draw(self, screen, color):
        """нарисовать квадрат"""
        get_coords = lambda x, y: (MARGIN + x * self.__size, MARGIN + y * self.__size, self.__size, self.__size)
        pg.draw.rect(screen, color, get_coords(self.x, self.y))

    def __repr__(self) -> str:
        return f'Cell {{x: {self.__x}, y: {self.y}, size: {self.__size}}}'