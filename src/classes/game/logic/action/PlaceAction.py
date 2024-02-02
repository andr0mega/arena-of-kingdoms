from classes.game.logic.action.GameAction import GameAction
from classes.game.logic.GameBoard import GameCoordinate
from classes.game.logic.action.GameAction import ActionType
from classes.game.logic.unit.Unit import Unit


class PlaceAction(GameAction):
    def __init__(self, onField: GameCoordinate, unit: Unit):
        self.onField = onField
        self.unit = unit
        super().__init__(ActionType.PLACE)