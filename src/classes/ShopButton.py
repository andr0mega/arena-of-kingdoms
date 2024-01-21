import pygame
from classes.ScreenElement import ScreenElement
from const.colors import *


class ShopButton(ScreenElement):
    def __init__(self, canvas, shop):
        super().__init__(canvas, COLOR_SHOP_ICON, hoverable=True)

        self.font = pygame.font.SysFont("Rockwell", 38)
        self.border_radius = 20

        self.shop = shop

    def set_dimensions(self):
        width_canvas, _ = super().get_canvas_dimensions()

        self.width = 150
        self.height = 60
        self.top = self.margin_top
        self.left = width_canvas - self.margin_right - self.width

    def draw_self(self):
        super().draw_self()

        shop_icon_text = "Shop"

        if self.shop.isopen:
            shop_icon_text = "Back"

        render_text = self.font.render(shop_icon_text, True, COLOR_SHOP_TEXT)
        text_left = self.left + (self.width - render_text.get_width()) / 2
        text_top = self.top + (self.height - render_text.get_rect()[3]) / 2
        self.canvas.blit(render_text, (text_left, text_top))

    def on_click(self):
        if self.shop.isopen:
            self.shop.close_shop()
        else:
            self.shop.open_shop()

    def open_shop(self):
        self.shop.open_shop()

    def close_shop(self):
        self.shop.close_shop()
