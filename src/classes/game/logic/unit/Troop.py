from classes.game.logic.unit.Unit import Unit

class Troop(Unit):
    def __init__(self, name: str, display_name: str, health: int, offense: int, defense: int, upkeep: int):
        self.display_name = display_name
        self.name = name
        self.health = health
        self.offense = offense
        self.defense = defense
        self.upkeep = upkeep
        super().__init__(name)