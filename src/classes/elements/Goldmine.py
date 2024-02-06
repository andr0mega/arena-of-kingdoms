from const.params import *
from classes.elements.Building import Building
from const.sprites import SPRITES


class Goldmine(Building):
    def __init__(self, name):
        super().__init__(
            name,
            cost=GOLDMINE_COST,
            health=GOLDMINE_HEALTH,
            blocking=GOLDMINE_BLOCKING,
            production=GOLDMINE_PRODUCTION,
            description=GOLDMINE_DESCRIPTION,
            image=SPRITES["goldmine"],
        )
