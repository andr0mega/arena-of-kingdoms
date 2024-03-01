import math
from classes.ScreenElement import ScreenElement
from const.colors import COLOR_WINDOW
from const.params import MARGIN_TOP, MARGIN_BOTTOM, MARGIN_RIGHT
from classes.game.logic.GameHandler import GameHandler
from classes.InventoryCard import InventoryCard


class Inventory(ScreenElement):
    def __init__(self, canvas):
        self.cards = None
        super().__init__(canvas, COLOR_WINDOW)

        self.game_handler = GameHandler.get_instance()

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

        if not len(self.game_handler.get_current_player().inventory):
            return
        
        self.cards = [InventoryCard(self.canvas, card_info) for card_info in self.game_handler.get_current_player().inventory]

        card_width = self.width
        card_height = self.width / 3 * 4

        for card in self.cards:
            card.adjust_dimensions(
                self.left,
                self.top + self.height - card_height,
                card_width,
                card_height
            )

            card.draw_self()

    def on_click(self):
        pass
