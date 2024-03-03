from classes.game.logic.unit.Unit import Unit


class Building(Unit):
    def __init__(
        self, name: str, display_name: str, health: int, blocking: bool, production: int
    ):
        self.name = name
        self.display_name = display_name
        self.health = health
        self.max_health = health
        self.blocking = blocking
        self.production = production
