from GameAction import GameAction
from GameBoard import GameCoordinate
from GameAction import ActionType


class MoveAction(GameAction):
    def __init__(self, fromField: GameCoordinate, toField: GameCoordinate):
        self.fromField = fromField
        self.toField = toField
        super().__init__(ActionType.MOVE)