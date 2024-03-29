import pygame
from classes.game.logic.GameHandler import GameHandler
from classes.CardLayout import CardLayout
from classes.ScreenElement import ScreenElement
from classes.ShopCard import ShopCard
from const.colors import *
from const.params import *


class Shop(ScreenElement):
    def __init__(self, canvas):
        super().__init__(canvas, COLOR_SHOP)
        gameHandler = GameHandler.get_instance()
        self.shop_items = [*(gameHandler.game_config.buildings), *(gameHandler.game_config.troops)]
        #self.shop_items = [*json.loads(TROOPS), *json.loads(BUILDINGS)]
        print(f"shop items:{str(self.shop_items)} ")

        def create_shop_card(card_info):
            card = ShopCard(
                canvas,
                card_info=card_info,
                shop=self,
            )
            return card

        self.shop_cards = [create_shop_card(card_info) for card_info in self.shop_items]

        self.card_layout = CardLayout(canvas, self.shop_cards, self)

        self.isopen = False

    def set_dimensions(self):
        _, height_canvas = super().get_canvas_dimensions()
        self.height = height_canvas - self.margin_top - self.margin_bottom
        self.width = self.height
        self.left = self.margin_left
        self.top = self.margin_top

    def on_click(self, mouse_button):
        pass

    def draw_self(self):
        if not self.isopen:
            return

        self.set_dimensions()

        shop_background_rect = pygame.rect.Rect(
            self.margin_left - RECT_BORDER,
            self.margin_top - RECT_BORDER,
            self.height + 2 * RECT_BORDER,
            self.width + 2 * RECT_BORDER,
        )

        pygame.draw.rect(self.canvas, COLOR_SHOP_BACKGROUND, shop_background_rect)

        super().draw_self()

    def open_shop(self):
        self.isopen = True

    def close_shop(self):
        self.isopen = False
