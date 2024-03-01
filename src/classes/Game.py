from classes.EndTurnButton import EndTurnButton
from classes.Board import Board
from classes.Shop import Shop
from classes.ShopButton import ShopButton
from classes.Infobox import (
    PlayerInfobox,
    TileInfobox
)
from classes.game.logic.GameHandler import GameHandler
from const.colors import *
from classes.Inventory import Inventory

class Game:
    def __init__(self, canvas):
        self.canvas = canvas

    def initialize_game(self):
        # Initialize Board and Players
        self.board = Board(self.canvas, GameHandler.get_instance().board.width)

        # Initialize Screen elements
        self.tiles = self.board.get_tiles()

        self.shop = Shop(self.canvas)
        self.shop_button = ShopButton(self.canvas, self.shop, self.board)
        self.end_turn_button = EndTurnButton(self.canvas, self.end_phase)
        self.player_infobox = PlayerInfobox(self.canvas)
        self.tile_infobox = TileInfobox(self.canvas)
        self.inventory = Inventory(self.canvas)

        self.draw_self()

    def draw_self(self):
        self.elements = [
            self.board,
            *self.tiles,
            self.shop,
            self.shop_button,
            self.end_turn_button,
            self.player_infobox,
            self.tile_infobox,
            self.shop.card_layout,
            *self.shop.shop_cards,
            self.inventory,
            *self.inventory.cards
        ]

        for element in self.elements:
            if not element:
                continue
            element.screen_rect = None
            element.draw_self()

    def end_phase(self):
        turn_ended = GameHandler.get_instance().end_turn()

