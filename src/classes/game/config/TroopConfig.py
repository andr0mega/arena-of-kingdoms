from classes.game.logic.unit.Troop import Troop


class TroopConfig:
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
        self.display_name = display_name
        self.name = name
        self.cost = cost
        self.health = health
        self.offense = offense
        self.defense = defense
        self.speed = speed
        self.upkeep = upkeep
        self.description = description

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
