import math
from collections import Counter
from random import choices
from typing import Tuple

from Cell import Cell
from CheckField import CheckField
from TypeCell import TypeCell
from config import *


class Logic:
    def __init__(self, size_x=0, size_y=0, nums_banned_cell=0) -> None:
        self.__size_x = size_x
        self.__size_y = size_y
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

    def __add_general_covered_cells(self, field_action):
        general_covered_cells = field_action & self.__set_covered_cell
        self.__counter_general_covered_cells += Counter(general_covered_cells)

    def __del_general_covered_cells(self, field_action):
        set_remove = set()
        general_covered_cells = field_action & self.__set_covered_cell
        for pos in general_covered_cells:
            self.__counter_general_covered_cells[pos] -= 1
            if self.__counter_general_covered_cells[pos] < 0:
                self.__counter_general_covered_cells.pop(pos)
            else:
                set_remove.add(pos)
        return set_remove

    def make_move(self, position: Tuple[int, int], radius: int = 1):
        """сделать ход"""
        self.__stack_moves.append((position, radius))
        field_action_tower = self.__get_field_action_tower(*position, radius)
        self.__add_general_covered_cells(field_action_tower)
        self.__set_covered_cell |= field_action_tower
        self.__set_position_towers.add(position)
        self.__set_free_cells -= field_action_tower
        self.__set_free_cells.remove(position)

    def undo_move(self):
        """отменить ход"""
        position, radius = self.__stack_moves.pop()
        field_action_tower = self.__get_field_action_tower(*position, radius)
        field_action_tower -= self.__del_general_covered_cells(field_action_tower)
        self.__set_covered_cell -= field_action_tower
        self.__set_position_towers.remove(position)
        self.__set_free_cells |= field_action_tower
        self.__set_free_cells.add(position)

    def __get_possible_moves(self):
        return self.__set_free_cells

    def is_end(self):
        """Конец игры?"""
        return len(self.__set_free_cells) == 0

    def evaluation(self) -> int:
        """оценивание карты"""
        res = 0
        if len(self.__set_free_cells) == 0:
            res = len(self.__set_position_towers)
        else:
            res = len(self.__set_position_towers) / len(self.__set_free_cells)
        return int(res * 100)
    def make_best_move(self):
        bestScore = -math.inf
        bestMove = None
        for move in self.__get_possible_moves():
            self.make_move(move)
            score = self.minimax(False)
            self.undo_move()
            if (score > bestScore):
                bestScore = score
                bestMove = move
        self.make_move(move)

    def minimax(self, isMaxTurn):
        if self.is_end():
            return self.evaluation()

        scores = []
        for move in self.__get_possible_moves():
            self.make_move(move)
            scores.append(self.minimax(not isMaxTurn))
            self.undo_move()
        return max(scores) if isMaxTurn else min(scores)




