import math
import pygame
from classes.ScreenElement import ScreenElement
from const.colors import COLOR_SHOP_CARD, COLOR_SHOP_TEXT
from const.sprites import SPRITES


class ShopCard(ScreenElement):
    def __init__(self, canvas, card_info, shop):
        self.left = 0
        self.top = 0
        self.width = 0
        self.height = 0

        super().__init__(canvas, COLOR_SHOP_CARD, hoverable=True)

        self.border_radius = 8
        self.title_font_size = 28
        self.title_font = pygame.font.SysFont(
            "Rockwell", self.title_font_size, bold=True
        )
        self.description_font_size = 18
        self.description_font = pygame.font.SysFont(
            "Rockwell", self.description_font_size
        )
        self.card_info = card_info
        self.shop = shop

    def set_dimensions(self):
        pass

    def draw_self(self):
        if not self.shop.isopen:
            return

        super().draw_self()

        # Render card image
        image_width = int(self.width * 0.7)
        image_height = image_width
        tile_top = self.top + self.height / 10
        tile_center_left = self.left + self.width / 2 - image_width / 2

        image_name = self.card_info["name"]

        scaled_image = pygame.transform.smoothscale(
            SPRITES[image_name], (image_width, image_height)
        )

        self.canvas.blit(scaled_image, (tile_center_left, tile_top))

        # Render card title
        title_font_size = math.floor(self.width / 8)

        # Don't re-create the font if it's the same size
        if self.title_font_size != title_font_size:
            self.title_font = pygame.font.SysFont(
                "Rockwell", title_font_size, bold=True
            )
            self.title_font_size = title_font_size

        text = self.card_info["display_name"]

        render_text = self.title_font.render(text, True, COLOR_SHOP_TEXT)
        text_left = self.left + self.width / 2 - render_text.get_width() / 2
        text_top = self.top + (self.height / 10) * 7 - render_text.get_height()
        self.canvas.blit(render_text, (text_left, text_top))

        # Render card description
        description = self.card_info["description"]

        description_1 = ""
        description_2 = ""

        # Split the description into two lines if it's too long
        if len(description) > 25:
            description_1 = description[: description.rfind(" ", 0, 25)]
            description_2 = description[description.rfind(" ", 0, 25) :]
        else:
            description_1 = description

        desc_font_size = math.floor(self.width / 12)

        # Don't re-create the font if it's the same size
        if self.description_font_size != desc_font_size:
            self.description_font = pygame.font.SysFont("Rockwell", desc_font_size)
            self.description_font_size = desc_font_size

        render_text = self.description_font.render(description_1, True, COLOR_SHOP_TEXT)
        text_left = self.left + self.width / 2 - render_text.get_width() / 2
        text_top = self.top + (self.height / 10) * 7.5
        self.canvas.blit(render_text, (text_left, text_top))

        if len(description_2) > 0:
            render_text = self.description_font.render(
                description_2, True, COLOR_SHOP_TEXT
            )
            text_left = self.left + self.width / 2 - render_text.get_width() / 2
            text_top = self.top + (self.height / 10) * 8.3
            self.canvas.blit(render_text, (text_left, text_top))

    def adjust_dimensions(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def on_click(self):
        print(f"Clicked on {self.card_info['name']}")
        pass
