from classes.game.logic.unit.Troop import Troop
from classes.game.logic.unit.Unit import Unit


class GamePlayer:
    def __init__(self, nr, name, color, startBalance):
        self.nr = nr
        self.name = name
        self.color = color
        self.balance = startBalance
        self.units = []

    def add_unit(self, unit: Unit):
        self.units.append(unit)
    
    def reduce_balance(self, reduction_value: int):
        if(self.balance - reduction_value < 0):
            raise ValueError(f"Cannot reduce player balance with value: {str(reduction_value)}. (Current balance: {str(self.balance)})")
        else:
            self.balance -= reduction_value

    def get_units_of_type(self, unit_name: str):
        return [unit for unit in self.units if unit.name == unit_name]
