import math
import pygame
from classes.ScreenElement import ScreenElement
from classes.game.logic.GameHandler import GameHandler
from const.colors import COLOR_CARD, COLOR_SHOP_TEXT, COLOR_CARD_BORDER
from const.sprites import SPRITES


class InventoryCard(ScreenElement):
    def __init__(self, canvas, card_info):
        self.left = 0
        self.top = 0
        self.width = 0
        self.height = 0

        super().__init__(canvas, COLOR_CARD, hoverable=True)

        self.border_radius = 8
        self.title_font_size = 28
        self.title_font = pygame.font.SysFont(
            "Rockwell", self.title_font_size, bold=True
        )

        self.card_info = card_info
        self.game_handler = GameHandler.get_instance()

    def set_dimensions(self):
        pass

    def draw_self(self):

        card_border = pygame.rect.Rect(
            self.left - 2,
            self.top - 2,
            self.width + 4,
            self.height + 4
        )

        pygame.draw.rect(self.canvas, COLOR_CARD_BORDER, card_border, border_radius=10)

        super().draw_self()

        # Render card image
        image_width = int(self.width * 0.7)
        image_height = image_width
        image_top = self.top + (self.height / 10) * 1.5
        image_center_left = self.left + self.width / 2 - image_width / 2

        image_name = self.card_info.name

        scaled_image = pygame.transform.smoothscale(
            SPRITES[image_name], (image_width, image_height)
        )

        self.canvas.blit(scaled_image, (image_center_left, image_top))

        # Render card title
        title_font_size = math.floor(self.width / 8)

        # Don't re-create the font if it's the same size
        if self.title_font_size != title_font_size:
            self.title_font = pygame.font.SysFont(
                "Rockwell", title_font_size, bold=True
            )
            self.title_font_size = title_font_size

        text = self.card_info.display_name

        render_text = self.title_font.render(text, True, COLOR_SHOP_TEXT)
        text_left = self.left + self.width / 2 - render_text.get_width() / 2
        text_top = self.top + (self.height / 10) * 1.5 - render_text.get_height()
        self.canvas.blit(render_text, (text_left, text_top))

    def adjust_dimensions(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def on_click(self):
        print(f"Clicked on {self.card_info.name} : {str(type(self.card_info))}")
