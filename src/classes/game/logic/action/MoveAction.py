from classes.game.logic.action.GameAction import GameAction
from classes.game.logic.action.GameAction import ActionType
from classes.game.logic.unit.Troop import Troop


class MoveAction(GameAction):
    def __init__(self, troop: Troop, fromField, toField, distance: int):
        self.troop = troop
        self.fromField = fromField
        self.toField = toField
        self.distance = distance
        super().__init__(ActionType.MOVE)
