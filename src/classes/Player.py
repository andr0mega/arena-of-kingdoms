from const.params import *

class Player:
    def __init__(self, name, nr, color, board):
        self.name = name
        self.color = color
        self.nr = nr
        self.balance = START_BALANCE

        self.board = board

    def get_tile_amount(self):
        return self.board.get_tiles_for_player(self)

