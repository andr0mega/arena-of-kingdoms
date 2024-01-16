import pygame
from const.colors import *
from helpers import get_hover_color


class Tile(pygame.rect.Rect):
    def __init__(self, left, top, width, height):
        self.set_dimensions(left, top, width, height)
        self.player = None
        self.hover = False
        super(Tile, self).__init__(
            self.left, self.top, self.width, self.height)

    def draw_self(self, canvas):
        pygame.draw.rect(canvas, self.get_color(), self)

    def set_dimensions(self, left, top, width, height):
        self.left = left + 1
        self.top = top + 1
        self.width = width - 1
        self.height = height - 1

    def get_color(self):
        if self.hover:
            if not self.player:
                return get_hover_color(COLOR_NEUTRAL_TILE)
            else:
                return get_hover_color(self.player.color)

        if self.player:
            return self.player.color

        return COLOR_NEUTRAL_TILE

    def set_player(self, player):
        self.player = player

    def set_hover(self, hover):
        self.hover = hover
