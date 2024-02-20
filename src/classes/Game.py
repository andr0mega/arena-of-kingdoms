from classes.EndTurnButton import EndTurnButton
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


class Game:
    def __init__(self, canvas):
        self.canvas = canvas

    def initialize_game(self):
        # Initialize Board and Players
        self.board = Board(self.canvas, GameHandler.get_instance().board.width)

        # Initialize Screen elements
        tiles = self.board.get_tiles()

        self.shop = Shop(self.canvas)
        self.shop_button = ShopButton(self.canvas, self.shop, self.board)
        self.end_turn_button = EndTurnButton(self.canvas, self.end_phase)
        self.player_infobox_border = PlayerInfoboxBorder(self.canvas)
        self.player_infobox = PlayerInfobox(self.canvas)
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
            self.shop.card_layout,
            *self.shop.shop_cards,
        ]

        self.draw_self()

    def draw_self(self):
        for element in self.elements:
            element.screen_rect = None
            element.draw_self()

    def end_phase(self):
        turn_ended = GameHandler.get_instance().end_turn()

