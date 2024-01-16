import pygame
from classes.Tile import Tile
from const.colors import *

class Board:
    def __init__(self, canvas, width=16):
        self.canvas = canvas
        self.width = width
        self.height = width

        self.margin_left = 50
        self.margin_top = 50
        self.margin_right = 50
        self.margin_bottom = 50
        
        self.set_board_dimensions()

        def create_tile(column, row):
            tile = Tile(
                self.margin_left + column * self.tile_width, 
                self.margin_top + row * self.tile_width, 
                self.tile_width, self.tile_width
            )
            return tile

        self.board = [[create_tile(column, row) for row in range(self.width)] for column in range(self.width)]

    def set_board_dimensions(self):
        _, _, self.width_canvas, self.height_canvas = self.canvas.get_rect()

        self.board_height = self.height_canvas - self.margin_top - self.margin_bottom
        self.board_width = self.board_height
        self.tile_width = int(self.board_width / self.width)
        self.tile_height = int(self.board_height / self.height)

    def draw_board(self):
        self.set_board_dimensions()

        board_rect = pygame.rect.Rect(self.margin_left, self.margin_top, self.tile_width * self.width + 1, self.tile_height * self.height + 1)
        pygame.draw.rect(self.canvas, COLOR_BOARD_BACKGROUND, board_rect)
        for column in range(len(self.board)):
            for row in range(len(self.board[column])):
                current_tile = self.board[column][row]
                current_tile.set_dimensions(
                    self.margin_left + column * self.tile_width, 
                    self.margin_top + row * self.tile_height, 
                    self.tile_width, self.tile_height
                )
                current_tile.draw_self(self.canvas)
    
    def get_tile(self, left, top):
        mouse_board_left = left - self.margin_left
        board_right = self.tile_width * self.width - 1
        mouse_board_top = top - self.margin_top
        board_bottom = self.tile_height * self.height - 1

        if 0 < mouse_board_left < board_right and 0 < mouse_board_top < board_bottom:
            column = int(mouse_board_left / self.tile_width)
            row = int(mouse_board_top / self.tile_height)
            return (column, row)
        return (None, None)

    def claim_tile(self, left, top, player):
        self.board[left][top].set_player(player)
    
    def reset_hover(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j].set_hover(False)

    def hover_tile(self, left, top):
        self.reset_hover()
        self.board[left][top].set_hover(True)


