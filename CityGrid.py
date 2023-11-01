from random import choices

from Cell import Cell
from CheckField import CheckField
from config import *


class CityGrid:
    def __init__(self, screen=None, size_x=None, size_y=None, size_cell=None, nums_banned_cell=0) -> None:
        self.__size_cell = size_cell
        self.__nums_banned_cell = nums_banned_cell
        self.__size_x = size_x
        self.__size_y = size_y
        self.__screen = screen
        self.__field = {(x, y): Cell(x, y, self.__size_cell) for x in range(size_x) for y in range(size_y)}
        self.__set_block_cells = self.__get_set_block_cells()
        self.__set_position_towers = self.__get_set_position_towers()
        self.__set_covered_cell = set()

    def __get_set_block_cells(self):
        """Получить позиции заблокированных блоков"""
        return set(choices(list(self.__field.keys()), k=self.__nums_banned_cell))

    def __get_set_position_towers(self):
        """Получить позиции башен"""
        lst_free_cell = list(set(self.__field.keys()) - self.__set_block_cells)
        return set(choices(lst_free_cell, k=2))

    @property
    def percentage_coverage(self) -> int:
        """Получить процент покрытия"""
        len_set_covered_cell = len(self.__set_covered_cell)
        if len_set_covered_cell > 0:
            return round(len(self.__set_covered_cell) / len(self.__field.keys()) * 100)
        else:
            return 100

    def get_field_action_tower(self, pos_x, pos_y, radius, is_save=False):
        """Получить поле действия башни"""
        set_cell = {CheckField.correct_position(x, y)
                    for y in range(pos_y - radius, pos_y + radius + 1)
                    for x in range(pos_x - radius, pos_x + radius + 1)}

        if is_save:
            self.__set_covered_cell |= set_cell
        return set_cell

    def draw_field_action_tower(self, position, radius):
        """нарисовать поле действия башни"""
        for pos in self.get_field_action_tower(*position, radius):
            if pos not in self.__set_position_towers:
                color = DIRTY_GREY if pos in self.__set_block_cells else YELLOW
                self.__field[pos].draw(self.__screen, color)

    def draw_towers(self):
        """нарисовать башню"""
        for tower in self.__set_position_towers:
            self.draw_field_action_tower(tower, 1)
            self.__field[tower].draw(self.__screen, RED)

    def draw(self):
        """нарисовать поле"""
        for pos, cell in self.__field.items():
            color = WHITE
            if pos in self.__set_block_cells:
                color = GREY
            cell.draw(self.__screen, color)
