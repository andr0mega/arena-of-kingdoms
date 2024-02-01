from GameAction import GameAction
from GameAction import ActionType


class MoveAction(GameAction):
    def __init__(self, unitName: str):
        self.unitName = unitName
        super().__init__(ActionType.BUY)