import os
import pygame
from classes.ScreenElement import ScreenElement
from const.colors import *
from const.sprites import SPRITES


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

        self.has_king = False

    def draw_self(self):
        if not self.board.is_visible:
            return

        super().draw_self()

        if self.has_king:
            image_height = int(self.height * 0.75)
            image_width = int(self.width * 0.75)
            tile_center_top = self.top + self.height / 2 - image_height / 2
            tile_center_left = self.left + self.width / 2 - image_width / 2

            scaled_image = pygame.transform.smoothscale(
                SPRITES['king_big'], (image_width, image_height))

            self.canvas.blit(scaled_image, (tile_center_left, tile_center_top))

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
