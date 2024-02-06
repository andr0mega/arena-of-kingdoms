from classes.game.logic.unit.Unit import Unit


class Building(Unit):
    def __init__(
        self, name: str, display_name: str, health: int, blocking: bool, production: int
    ):
        self.name = name
