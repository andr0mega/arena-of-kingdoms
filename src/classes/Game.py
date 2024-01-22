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
        self.player_cycle = []

    def initialize_game(self):
        #Initialize Screen elements
        self.board = Board(self.canvas)
        self.shop = Shop(self.canvas)
        self.shop_button = ShopButton(self.canvas, self.shop, self.board)
        self.end_turn_button = EndTurnButton(self.canvas, self.end_phase)

        tiles = self.board.get_tiles()

        self.elements = [
            self.board,
            self.shop,
            self.shop_button,
            self.end_turn_button,
            *tiles
        ]

        self.draw_self()

        #Initialize Players
        for i in range(self.nr_players):
            player = Player(f'Player {i+1}', i, PLAYER_COLORS[i])
            self.players[player.nr] = player
            self.player_cycle.append(player.nr)
        
        #Initialize First turn and deployment phase
        self.player_cycle_index = 0
        globals.active_player = self.players[self.player_cycle[self.player_cycle_index]]
        globals.turn = 1
        globals.phase = "deployment"


    def draw_self(self):
        for element in self.elements:
            element.draw_self()

    def start_gearup_phase(self):
        globals.phase = "gearup"

    def start_combat_phase(self):
        globals.phase = "combat"

    def start_income_phase(self):
        globals.phase = "income"

    def end_phase(self):
        globals.deployment_lock = False
        if self.player_cycle_index == self.nr_players - 1:
            self.player_cycle_index = 0
        else:
            self.player_cycle_index += 1

        globals.active_player = self.players[self.player_cycle[self.player_cycle_index]]

        if globals.active_player == self.players[0]:
            if globals.phase == "deployment":
                self.start_gearup_phase()
            elif globals.phase == "gearup":
                self.start_combat_phase()
            elif globals.phase == "combat":
                self.start_income_phase()
            elif globals.phase == "income":
                self.start_gearup_phase()



    def update_active_player(self):
        pass

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
