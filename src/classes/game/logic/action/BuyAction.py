from classes.game.logic.action.GameAction import ActionType
from classes.game.logic.action.GameAction import GameAction
from classes.game.logic.unit import Unit


class BuyAction(GameAction):
    def __init__(self, unit: Unit):
        self.unit = unit
        super().__init__(ActionType.BUY)
