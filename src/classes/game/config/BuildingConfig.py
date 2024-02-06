from classes.game.logic.unit.Building import Building


class BuildingConfig:
    def __init__(
        self,
        display_name: str,
        name: str,
        cost: int,
        health: int,
        blocking: bool,
        production: int,
        description: str,
    ):
        self.display_name = display_name
        self.name = name
        self.cost = cost
        self.health = health
        self.blocking = blocking
        self.production = production
        self.description = description

    def create_from_config(self) -> Building:
        return Building(
            self.name, self.display_name, self.health, self.blocking, self.production
        )
