from const.params import *
from Field import *


class GameBoard:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.create_fields(width, height)

    def create_fields(self, width, height):
        self.fields = [[Field.builder().build() for _ in range(width)] for _ in range(height)]

class GameCoordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y