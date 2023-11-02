from typing import Tuple

from config import *


class CheckField:

    @classmethod
    def correct_position(cls, x, y):
        correct_coordinate = lambda cell, cell_size: cell >= 0 and cell < cell_size
        return correct_coordinate(x, CELL_QTY_X) and correct_coordinate(y, CELL_QTY_Y)
