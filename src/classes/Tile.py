import pygame
from classes.ScreenElement import ScreenElement
from const.colors import *


class Tile(ScreenElement):
    def __init__(self, canvas, left, top, width, height, tile_pos, on_tile_click, board):
        self.left = left + 1
        self.top = top + 1
        self.width = width - 1
        self.height = height - 1

        super().__init__(canvas, COLOR_NEUTRAL_TILE, hoverable=True)

        self.on_tile_click = on_tile_click
        self.tile_pos = tile_pos
        self.board = board
        self.player = None

    def draw_self(self):
        if not self.board.is_visible:
            return

        super().draw_self()

    def set_dimensions(self):
        pass

    def adjust_dimensions(self, left, top, width, height):
        self.left = left + 1
        self.top = top + 1
        self.width = width - 1
        self.height = height - 1

    def get_color(self):
        if self.player:
            return self.player.color

        return COLOR_NEUTRAL_TILE

    def set_player(self, player):
        self.player = player

    def on_click(self):
        self.on_tile_click(self.tile_pos)
