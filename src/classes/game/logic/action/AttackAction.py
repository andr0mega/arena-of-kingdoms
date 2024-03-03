from classes.game.logic.action.GameAction import GameAction
from classes.game.logic.action.GameAction import ActionType
from classes.game.logic.unit.Troop import Troop


class AttackAction(GameAction):
    def __init__(self, attackTroop: Troop, attackedTroop: Troop, fromField, toField):
        self.attackTroop = attackTroop
        self.attackedTroop = attackedTroop
        self.fromField = fromField
        self.toField = toField
        super().__init__(ActionType.ATTACK)
