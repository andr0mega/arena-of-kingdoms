from classes.game.config.UnitConfig import UnitConfig
from classes.game.logic.unit.Troop import Troop


class TroopConfig(UnitConfig):
    def __init__(
        self,
        display_name: str,
        name: str,
        cost: int,
        health: int,
        offense: int,
        defense: int,
        speed: int,
        upkeep: int,
        description: str,
    ):
        super().__init__(name, display_name, description, cost)
        self.health = health
        self.offense = offense
        self.defense = defense
        self.speed = speed
        self.upkeep = upkeep

    def create_from_config(self) -> Troop:
        return Troop(
            self.name,
            self.display_name,
            self.health,
            self.offense,
            self.defense,
            self.speed,
            self.upkeep,
        )
