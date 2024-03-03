import math
from classes.ScreenElement import ScreenElement
from const.colors import COLOR_WINDOW
from const.params import *
from classes.game.logic.GameHandler import GameHandler
from classes.InventoryCard import InventoryCard


class Inventory(ScreenElement):
    def __init__(self, canvas):
        self.cards = []
        super().__init__(canvas, COLOR_WINDOW)

        self.game_handler = GameHandler.get_instance()

        self.rows = 5

        self.margin_left = 10
        self.margin_top = 120
        self.margin_bottom = 120
        self.margin_right = 10

        self.game_handler.subscribe_event_listener(self.on_inventory_change)

    def on_inventory_change(self, event):
        if event is EVENTS["INVENTORY_CHANGE"]:
            self.cards = [
                InventoryCard(self.canvas, card_info, index)
                for index, card_info in enumerate(
                    self.game_handler.get_current_player().inventory
                )
            ]

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

        card_width = self.width
        card_height = self.width / 3 * 4

        for i, card in enumerate(self.cards):
            card.adjust_dimensions(
                self.left,
                self.top + i * (self.height - card_height) // 6,
                card_width,
                card_height,
            )

    def get_cards(self):
        for card_index, card in enumerate(self.cards):
            card.card_index = card_index

        hovered_cards = list(filter(lambda el: el.hover is True, self.cards))
        hovered_card = hovered_cards[0] if len(hovered_cards) > 0 else None
        visual_hovered_card = None

        if hovered_card is not None:
            hovered_card.card_index = len(self.cards)
            visual_hovered_card = InventoryCard(self.canvas, hovered_card.card_info, hovered_card.card_index, True)
            visual_hovered_card.adjust_dimensions(
                hovered_card.left,
                hovered_card.top,
                hovered_card.width,
                hovered_card.height,
            )
            visual_hovered_card.on_hover(True)

        return [*self.cards, visual_hovered_card]

    def on_click(self, mouse_button):
        pass
