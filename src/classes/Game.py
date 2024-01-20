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
        self.turn_cycle = []

    def initialize_game(self):
        for i in range(self.nr_players):
            player = Player(f'Player {i+1}', i, PLAYER_COLORS[i])
            self.players[player.nr] = player
            self.turn_cycle.append(player.nr)

        self.screen = Screen(self.canvas)        
        self.board = Board(self.canvas)
        self.shop = Shop(self.canvas)
        self.board.draw_board()
        self.shop.draw_shop_icon()
        self.screen.draw_end_turn_icon()

    def start_round(self):
        self.start_turn()

    def start_turn(self):
        for player in self.players.values():
            if player.nr == self.turn_cycle[0]:
                player.enable()
        
    def end_turn(self):
        for player in self.players.values():
            if player.active == True:
                player.active = False
        del self.turn_cycle[0]
        self.end_phase()

    def end_phase(self):
        if len(self.turn_cycle):
            #do something
        else:
            pass
    
