from Player import Player
from Board import Board
from Shop import Shop
from Screen import Screen
from const.colors import *


class Game:
    def __init__(self, canvas, nr_players):
        self.canvas = canvas
        self.nr_players = nr_players
        self.players = {}

    def initialize_game(self):
        for i in range(self.nr_players):
            player = Player(f'Player {i+1}', PLAYER_COLORS[i])
            self.players[player.name] = player

        self.screen = Screen(self.canvas)        
        self.board = Board(self.canvas)
        self.shop = Shop(self.canvas)
        self.board.draw_board()
        self.shop.draw_shop_icon()
        self.screen.draw_end_turn_icon()
    
