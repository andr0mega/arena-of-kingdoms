from const.params import *
from classes.elements.Purchasable import Purchasable

class Building(Purchasable):
    def __init__(self, name, cost, health, blocking, production, description, image):
        super().__init__(name, cost, description, image)
        self.health = health
        self.blocking = blocking
        self.production = production
        self.description = description
        self.image = image

    def get_image(self):
        return self.image