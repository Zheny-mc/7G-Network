from enum import Enum


class TypeCell(Enum):
    BLOCKED = -1
    FREE = 0
    COVERED = 1
    TOWER = 2

