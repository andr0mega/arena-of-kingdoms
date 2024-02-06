from const.params import *
from classes.elements.Unit import Unit
from const.sprites import SPRITES


class Warrior(Unit):
    def __init__(self, name):
        super().__init__(
            name,
            cost=WARRIOR_COST,
            health=WARRIOR_HEALTH,
            off=WARRIOR_OFF,
            deff=WARRIOR_DEFF,
            speed=WARRIOR_SPEED,
            upkeep=WARRIOR_UPKEEP,
            description=WARRIOR_DESCRIPTION,
            image=SPRITES["warrior"],
        )
