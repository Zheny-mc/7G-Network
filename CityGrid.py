from random import choices

from Cell import Cell
from CheckField import CheckField
from Logic import Logic
from config import *


class CityGrid:
    def __init__(self, screen=None) -> None:
        self.__screen = screen

    def draw(self, field):
        """нарисовать поле"""
        for cell, color in field.items():
            cell.draw(self.__screen, color)
