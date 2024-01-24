from const.params import *
from classes.elements.Unit import Unit
from const.sprites import SPRITES

class King(Unit):
    def __init__(self, name):
        super().__init__(name, 
                         cost=None, 
                         health=KING_HEALTH, 
                         off=KING_OFF, 
                         deff=KING_DEFF, 
                         speed=KING_SPEED, 
                         upkeep=KING_UPKEEP, 
                         description=KING_DESCRIPTION,
                         image = SPRITES["king"])
