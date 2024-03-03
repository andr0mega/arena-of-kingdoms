from classes.game.config.UnitConfig import UnitConfig
from classes.game.logic.unit.Troop import Troop


class TroopConfig(UnitConfig):
    def __init__(
        self,
        display_name: str,
        owner_name: str,
        name: str,
        cost: int,
        health: int,
        offense: int,
        defense: int,
        speed: int,
        upkeep: int,
        attack_range: int,
        description: str,
        
    ):
        super().__init__(name, display_name, owner_name, description, cost)
        self.health = health
        self.offense = offense
        self.defense = defense
        self.speed = speed
        self.upkeep = upkeep
        self.attack_range = attack_range
        

    def create_from_config(self) -> Troop:
        return Troop(
            self.name,
            self.display_name,
            self.owner_name,
            self.health,
            self.offense,
            self.defense,
            self.speed,
            self.upkeep,
            self.attack_range,
        )
