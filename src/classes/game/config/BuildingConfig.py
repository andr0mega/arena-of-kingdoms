from classes.game.config.UnitConfig import UnitConfig
from classes.game.logic.unit.Building import Building


class BuildingConfig(UnitConfig):
    def __init__(
        self,
        display_name: str,
        owner_name: str,
        name: str,
        cost: int,
        health: int,
        blocking: bool,
        production: int,
        description: str,
    ):
        super().__init__(name, display_name, owner_name, description, cost)
        self.health = health
        self.blocking = blocking
        self.production = production

    def create_from_config(self) -> Building:
        return Building(
            self.name, self.display_name, self.owner_name, self.health, self.blocking, self.production
        )
