from const.params import *
from classes.game.logic.Field import Field


class GameBoard:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.create_fields(width, height)

    def create_fields(self, width, height):
        self.fields = [
            [Field.builder().build() for _ in range(width)] for _ in range(height)
        ]
    
    @classmethod
    def calculate_distance(cls, coordinate_from, coordinate_to):
        #distance is equal to the max diff in coordinates (as diagonal movement is also just 1 distance)
        return max(abs(coordinate_to.y - coordinate_from.y), abs(coordinate_to.x - coordinate_from.x))


class GameCoordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
