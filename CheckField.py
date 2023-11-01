from typing import Tuple

from config import *


class CheckField:
    @classmethod
    def correct_coordinate(cls, coordinate: int) -> int:
        if coordinate < 0:
            return 0
        elif coordinate >= CELL_QTY:
            return CELL_QTY-1
        else:
            return coordinate

    @classmethod
    def correct_position(cls, x, y) -> Tuple[int, int]:
        return cls.correct_coordinate(x), cls.correct_coordinate(y)