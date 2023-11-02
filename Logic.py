from collections import Counter
from random import choices
from typing import Tuple

from Cell import Cell
from CheckField import CheckField
from config import *


class Logic:
    def __init__(self, size_x=0, size_y=0, radius=0, nums_banned_cell=0) -> None:
        self.__size_x = size_x
        self.__size_y = size_y
        self.__radius = radius
        self.__field = {(x, y) for x in range(size_x) for y in range(size_y)}
        self.__set_block_cells = self.__get_set_block_cells(nums_banned_cell)
        self.__set_free_cells = self.__field - self.__set_block_cells
        self.__set_position_towers = set()
        self.__set_covered_cell = set()
        self.__stack_moves = []
        self.__counter_general_covered_cells = Counter()


    @property
    def field(self):
        '''Получить поле для отрисовки'''
        def type_to_color(position):
            if position in self.__set_block_cells:
                return GREY
            elif position in self.__set_free_cells:
                return WHITE
            elif position in self.__set_position_towers:
                return RED
            elif position in self.__set_covered_cell:
                return DIRTY_GREY

        return {Cell(*pos): type_to_color(pos) for pos in self.__field}

    def __get_set_block_cells(self, nums_banned_cell: int):
        """Получить позиции заблокированных блоков"""
        return set(choices(list(self.__field), k=nums_banned_cell))

    def __get_field_action_tower(self, pos_x, pos_y, radius):
        """Получить поле действия башни"""
        return { (x, y) for y in range(pos_y - radius, pos_y + radius + 1)
                for x in range(pos_x - radius, pos_x + radius + 1)
                if CheckField.correct_position(x, y) and (x != pos_x or y != pos_y) }

    def make_move(self, position: Tuple[int, int], radius: int):
        """сделать ход"""
        self.__stack_moves.append((position, radius))
        field_action_tower = self.__get_field_action_tower(*position, radius)
        self.__set_covered_cell |= field_action_tower
        self.__set_position_towers.add(position)
        self.__set_free_cells -= field_action_tower

    def __get_possible_moves(self):
        return self.__set_free_cells

    def is_end(self):
        """Конец игры?"""
        return len(self.__set_free_cells) == 0

    def optimize_towers(self):
        """Алгоритм оптимизации размещения башен"""
        if self.is_end():
            return

        cell = self.__get_possible_moves().pop()
        self.make_move(cell, self.__radius)





