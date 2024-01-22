import pygame
from classes.ScreenElement import ScreenElement
from classes.Tile import Tile
from const.colors import *
import const.globals as globals

class Board(ScreenElement):
    def __init__(self, canvas, width=16):
        self.tile_rows = width
        self.tile_columns = width

        super().__init__(canvas, COLOR_BOARD_BACKGROUND)

        def create_tile(column, row):
            tile = Tile(
                canvas,
                left=self.margin_left + column * self.tile_width,
                top=self.margin_top + row * self.tile_width,
                width=self.tile_width, height=self.tile_width,
                on_tile_click=self.on_tile_click,
                tile_pos=(column, row)
            )
            return tile

        self.board = [[create_tile(column, row) for row in range(
            self.tile_rows)] for column in range(self.tile_rows)]

    def on_tile_click(self, tile):
        self.board[tile[0]][tile[1]].set_player(globals.active_player)

    def on_click(self):
        pass

    def get_tiles(self):
        tiles = []
        for column in self.board:
            for tile in column:
                tiles.append(tile)
        return tiles

    def set_dimensions(self):
        _, height_canvas = super().get_canvas_dimensions()
        base_height = height_canvas - self.margin_top - self.margin_bottom
        base_width = base_height
        self.tile_width = int(base_width / self.tile_rows)
        self.tile_height = int(base_height / self.tile_columns)

        self.left = self.margin_left
        self.top = self.margin_top

        self.width = self.tile_width * self.tile_rows + 1
        self.height = self.tile_height * self.tile_columns + 1

    def draw_self(self):
        super().draw_self()

        for column in range(len(self.board)):
            for row in range(len(self.board[column])):
                current_tile = self.board[column][row]
                current_tile.adjust_dimensions(
                    self.margin_left + column * self.tile_width,
                    self.margin_top + row * self.tile_height,
                    self.tile_width, self.tile_height
                )
