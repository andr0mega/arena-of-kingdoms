import pygame
from classes.ScreenElement import ScreenElement
from classes.Tile import Tile
from const.colors import *


class Board(ScreenElement):
    def __init__(self, canvas, width=16):
        self.tile_rows = width
        self.tile_columns = width

        super().__init__(canvas, COLOR_BOARD_BACKGROUND)

        def create_tile(column, row):
            tile = Tile(
                self.margin_left + column * self.tile_width,
                self.margin_top + row * self.tile_width,
                self.tile_width, self.tile_width
            )
            return tile

        self.board = [[create_tile(column, row) for row in range(
            self.tile_rows)] for column in range(self.tile_rows)]

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
                current_tile.set_dimensions(
                    self.margin_left + column * self.tile_width,
                    self.margin_top + row * self.tile_height,
                    self.tile_width, self.tile_height
                )
                current_tile.draw_self(self.canvas)

    def get_hovered_tile(self):
        left, top = pygame.mouse.get_pos()

        mouse_board_left = left - self.margin_left
        board_right = self.tile_width * self.tile_rows - 1
        mouse_board_top = top - self.margin_top
        board_bottom = self.tile_height * self.tile_columns - 1

        if 0 < mouse_board_left < board_right and 0 < mouse_board_top < board_bottom:
            column = int(mouse_board_left / self.tile_width)
            row = int(mouse_board_top / self.tile_height)
            return (column, row)
        return (None, None)

    def on_hover(self, hover):
        super().on_hover(hover)

        hovered_tile = self.get_hovered_tile()
        if hovered_tile != (None, None):
            self.hover_tile(hovered_tile[0], hovered_tile[1])
        else:
            self.reset_hover()

    def on_click(self):
        hovered_tile = self.get_hovered_tile()
        # TODO: claim tile for current player
        # self.board[left][top].set_player(player)
        pass

    def reset_hover(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j].set_hover(False)

    def hover_tile(self, left, top):
        self.reset_hover()
        self.board[left][top].set_hover(True)
