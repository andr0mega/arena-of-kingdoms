import pygame
from classes.ScreenElement import ScreenElement
from const.colors import *


class Shop(ScreenElement):
    def __init__(self, canvas):
        super().__init__(canvas, COLOR_SHOP)

        self.isopen = False

    def set_dimensions(self):
        _, height_canvas = super().get_canvas_dimensions()
        self.height = height_canvas - self.margin_top - self.margin_bottom
        self.width = self.height
        self.left = self.margin_left
        self.top = self.margin_top

    def on_click(self):
        pass

    def draw_self(self):
        if not self.isopen:
            return

        self.set_dimensions()

        shop_background_rect = pygame.rect.Rect(
            self.margin_left - 2, self.margin_top - 2, self.height + 4, self.width + 4)

        pygame.draw.rect(self.canvas, COLOR_SHOP_BACKGROUND,
                         shop_background_rect)

        super().draw_self()

    def open_shop(self):
        self.isopen = True

    def close_shop(self):
        self.isopen = False
