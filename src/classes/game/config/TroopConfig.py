class TroopConfig:
    def __init__(self, display_name: str, name: str, cost: int, health: int, offense: int, defense: int, speed: int, upkeep: int, description: str):
        self.display_name = display_name
        self.name = name
        self.cost = cost
        self.health = health
        self.offense = offense
        self.defense = defense
        self.speed = speed
        self.upkeep = upkeep
        self.description = description