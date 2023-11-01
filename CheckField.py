from typing import Tuple

from config import *


class CheckField:
    @classmethod
    def correct_coordinate(cls, coordinate: int, cell_size: str) -> int:
        if coordinate < 0:
            return 0
        elif coordinate >= cell_size:
            return cell_size-1
        else:
            return coordinate

    @classmethod
    def correct_position(cls, x, y) -> Tuple[int, int]:
        return cls.correct_coordinate(x, CELL_QTY_X), \
            cls.correct_coordinate(y, CELL_QTY_Y)