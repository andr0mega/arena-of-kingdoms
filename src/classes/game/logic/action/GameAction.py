from enum import Enum
from classes.game.logic.action.GameAction import ActionType

class GameAction:
    def __init__(self, type: ActionType):
        self.type = type


class ActionType(Enum):
    PLACE = 1
    MOVE = 2
    BUY = 3