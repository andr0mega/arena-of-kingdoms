from GameAction import GameAction
from GameBoard import GameCoordinate
from GameAction import ActionType
from classes.game.logic.unit.Unit import Unit


class MoveAction(GameAction):
    def __init__(self, onField: GameCoordinate, unit: Unit):
        self.onField = onField
        self.unit = unit
        super().__init__(ActionType.PLACE)