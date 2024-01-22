from classes.EndTurnButton import EndTurnButton
from classes.Player import Player
from classes.Board import Board
from classes.Shop import Shop
from classes.ShopButton import ShopButton
from const.colors import *
import const.globals as globals


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

        globals.active_player = self.players[self.turn_cycle[0]]

        self.board = Board(self.canvas)
        self.shop = Shop(self.canvas)
        self.shop_button = ShopButton(self.canvas, self.shop)
        self.end_turn_button = EndTurnButton(self.canvas)

        tiles = self.board.get_tiles()

        self.elements = [
            self.board,
            self.shop,
            self.shop_button,
            self.end_turn_button,
            *tiles
        ]

        self.draw_self()

    def draw_self(self):
        for element in self.elements:
            element.draw_self()


"""

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
    
"""
