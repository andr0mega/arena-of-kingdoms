from classes.game.logic.unit.Troop import Troop
from classes.game.logic.unit.Unit import Unit


class GamePlayer:
    def __init__(self, nr, name, color, startBalance):
        self.nr = nr
        self.name = name
        self.color = color
        self.balance = startBalance

    def add_unit(self, unit: Unit):
        self.units.append(unit)

