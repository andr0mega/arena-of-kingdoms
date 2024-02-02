from GameAction import GameAction
from GameAction import ActionType
from classes.elements.Unit import Unit


class BuyAction(GameAction):
    def __init__(self, unit: Unit):
        self.unit = unit
        super().__init__(ActionType.BUY)