import math
from classes.ScreenElement import ScreenElement
from const.colors import COLOR_WINDOW
from const.params import MARGIN_TOP, MARGIN_BOTTOM, MARGIN_RIGHT


class Inventory(ScreenElement):
    def __init__(self, canvas):
        super().__init__(canvas, (102, 102, 102))

        #self.cards = cards

        self.rows = 5

        self.margin_left = 10
        self.margin_top = 120
        self.margin_bottom = 120
        self.margin_right = 10

    def set_dimensions(self):
        width_canvas, height_canvas = super().get_canvas_dimensions()
        self.height = height_canvas - self.margin_top - self.margin_bottom
        self.width = (height_canvas - MARGIN_TOP - MARGIN_BOTTOM) / 4 - 12.5
        self.left = width_canvas - MARGIN_RIGHT - self.width
        self.top = self.margin_top

    def draw_self(self):
        super().draw_self()

        # for i, card in enumerate(self.cards):

        #     card_left = (
        #         self.margin_left + (i % self.columns) * self.width / self.columns
        #     )
        #     card_top = self.margin_top + i // (self.rows + 1) * self.height / self.rows
        #     card.adjust_dimensions(
        #         card_left + self.card_margin,
        #         card_top + self.card_margin,
        #         (self.width / self.columns) - 2 * self.card_margin,
        #         (self.height / self.rows) - 2 * self.card_margin,
        #     )
        #     card.draw_self()

    def on_click(self):
        pass
