from enum import Enum


class GameAction:
    def __init__(self, type):
        self.type = type


class ActionType(Enum):
    PLACE = 1
    MOVE = 2
    BUY = 3
