import math
from classes.ScreenElement import ScreenElement
from const.colors import COLOR_SHOP


class CardLayout(ScreenElement):
    def __init__(self, canvas, cards, shop):
        super().__init__(canvas, COLOR_SHOP)

        self.cards = cards
        self.shop = shop

        self.columns = 4
        self.rows = 3
        self.card_margin = 10

        self.margin_left = 40
        self.margin_top = 40
        self.margin_bottom = 40
        self.margin_right = 40

    def set_dimensions(self):
        _, height_canvas = super().get_canvas_dimensions()
        self.height = height_canvas - self.margin_top - self.margin_bottom
        self.width = self.height
        self.left = self.margin_left
        self.top = self.margin_top

    def draw_self(self):
        if not self.shop.isopen:
            return

        super().draw_self()

        for i, card in enumerate(self.cards):

            card_left = (
                self.margin_left + (i % self.columns) * self.width / self.columns
            )
            card_top = self.margin_top + i // (self.rows + 1) * self.height / self.rows
            card.adjust_dimensions(
                card_left + self.card_margin,
                card_top + self.card_margin,
                (self.width / self.columns) - 2 * self.card_margin,
                (self.height / self.rows) - 2 * self.card_margin,
            )
            card.draw_self()

    def on_click(self, mouse_button):
        pass
