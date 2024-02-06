from classes.EndTurnButton import EndTurnButton
from classes.Player import Player
from classes.Board import Board
from classes.Shop import Shop
from classes.ShopButton import ShopButton
from classes.Infobox import (
    PlayerInfoboxBorder,
    PlayerInfobox,
    TileInfoboxBorder,
    TileInfobox,
)
from classes.game.logic.GameHandler import GameHandler
from const.colors import *
import const.globals as globals

from classes.elements import *


class Game:
    def __init__(self, canvas, nr_players):
        self.canvas = canvas
        self.nr_players = nr_players
        self.players = {}
        self.player_cycle = []

    def initialize_game(self):
        # Initialize Board and Players
        self.board = Board(self.canvas)
        for i in range(self.nr_players):
            player = Player(f"Player {i+1}", i, PLAYER_COLORS[i], self.board)
            player.add_unit(Goldmine("king"))
            self.players[player.nr] = player
            self.player_cycle.append(player.nr)

        # Initialize First turn and deployment phase
        self.player_cycle_index = 0
        globals.active_player = self.players[self.player_cycle[self.player_cycle_index]]
        globals.turn = 1
        globals.phase = "deployment"

        # Initialize Screen elements
        tiles = self.board.get_tiles()

        self.shop = Shop(self.canvas)
        self.shop_button = ShopButton(self.canvas, self.shop, self.board)
        self.end_turn_button = EndTurnButton(self.canvas, self.end_phase)
        self.player_infobox_border = PlayerInfoboxBorder(self.canvas)
        self.player_infobox = PlayerInfobox(self.canvas, self.players)
        self.tile_infobox_border = TileInfoboxBorder(self.canvas)
        self.tile_infobox = TileInfobox(self.canvas)

        self.elements = [
            self.board,
            *tiles,
            self.shop,
            self.shop_button,
            self.end_turn_button,
            self.player_infobox_border,
            self.player_infobox,
            self.tile_infobox_border,
            self.tile_infobox,
        ]

        self.draw_self()

    def draw_self(self):
        for element in self.elements:
            element.screen_rect = None
            element.draw_self()

    def start_gearup_phase(self):
        globals.phase = "gearup"

    def start_combat_phase(self):
        globals.phase = "combat"

    def start_income_phase(self):
        globals.phase = "income"

    def end_phase(self):
        turn_ended = GameHandler.get_instance().end_turn()
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
