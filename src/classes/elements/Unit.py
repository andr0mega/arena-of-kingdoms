from const.params import *
from classes.elements.Purchasable import Purchasable


class Unit(Purchasable):
    def __init__(
        self, name, cost, health, off, deff, speed, upkeep, description, image
    ):
        super().__init__(name, cost, description, image)
        self.health = health
        self.off = off
        self.deff = deff
        self.speed = speed
        self.upkeep = upkeep
        self.description = description
        self.image = image

    def get_image(self):
        return self.image
