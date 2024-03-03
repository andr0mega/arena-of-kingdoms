import math
import pygame
from classes.ScreenElement import ScreenElement
from classes.game.logic.GameHandler import GameHandler
from const.colors import COLOR_CARD, COLOR_SHOP_TEXT
from const.sprites import SPRITES


class ShopCard(ScreenElement):
    def __init__(self, canvas, card_info, shop):
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
        self.description_font_size = 18
        self.description_font = pygame.font.SysFont(
            "Rockwell", self.description_font_size
        )
        self.stats_font_size = 18
        self.stats_font = pygame.font.SysFont(
            "Rockwell", self.stats_font_size
        )
        self.card_info = card_info
        self.shop = shop
        self.game_handler = GameHandler.get_instance()
        self.flipped = False

    def set_dimensions(self):
        pass

    def draw_self(self):
        if not self.shop.isopen:
            return

        super().draw_self()

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

        text_offset_ratio = 6.5

        # Check if card is flipped and display different card properties
        if not self.flipped:

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

            # Render card description
            description = self.card_info.description

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
            text_top = self.top + (self.height / 10) * text_offset_ratio
            self.canvas.blit(render_text, (text_left, text_top))

            if len(description_2) > 0:
                render_text = self.description_font.render(
                    description_2, True, COLOR_SHOP_TEXT
                )
                text_left = self.left + self.width / 2 - render_text.get_width() / 2
                text_top = self.top + (self.height / 10) * (text_offset_ratio + 0.8)
                self.canvas.blit(render_text, (text_left, text_top))

        elif self.flipped:
            # Render stats
            health = getattr(self.card_info, "health", None)
            offense = getattr(self.card_info, "offense", None)
            defense = getattr(self.card_info, "defense", None)
            speed = getattr(self.card_info, "speed", None)
            range = getattr(self.card_info, "attack_range", None)
            upkeep = getattr(self.card_info, "upkeep", None)
            production = getattr(self.card_info, "production", None)

            stats = [
                f"Health: {health}" if health else None,
                f"Offense: {offense}" if offense else None,
                f"Defense: {defense}" if defense else None,
                f"Speed: {speed}" if speed else None,
                f"Range: {range}" if range else None,
                f"Upkeep: {upkeep}/turn" if upkeep else None,
                f"Production: {production}/turn" if production else None,
            ]

            stats_font_size = math.floor(self.width / 12)

            # Don't re-create the font if it's the same size
            if self.stats_font_size != stats_font_size:
                self.stats_font = pygame.font.SysFont("Rockwell", stats_font_size)
                self.stats_font_size = stats_font_size
            
            text_top = self.top + self.height / 10

            for line in stats:
                if not line:
                    continue
                render_text = self.stats_font.render(line, True, COLOR_SHOP_TEXT)
                text_left = self.left + self.width / 5
                text_top = text_top + render_text.get_height() + text_offset_ratio
                self.canvas.blit(render_text, (text_left, text_top))

        self.render_price()

    def render_price(self):
        # Render price background
        price_background_color = tuple(color - 25 for color in COLOR_CARD)
        price_background_height = self.height / 10
        price_background_width = (self.width / 10) * 9
        price_background_left = self.left + self.width / 2 - price_background_width / 2
        price_background_top = self.top + (self.height / 10) * 8.6
        price_background_rect = pygame.rect.Rect(
            price_background_left,
            price_background_top,
            price_background_width,
            price_background_height,
        )
        pygame.draw.rect(
            self.canvas,
            price_background_color,
            price_background_rect,
            border_radius=6,
        )

        # Render price text
        price = str(self.card_info.cost)

        gold_icon_width = int(self.width / 12)

        render_text = self.description_font.render(price, True, COLOR_SHOP_TEXT)
        price_text_width = render_text.get_width()
        price_combined_width = price_text_width + gold_icon_width
        text_left = self.left + self.width / 2 - price_combined_width / 2
        text_top = self.top + (self.height / 10) * 8.7
        self.canvas.blit(render_text, (text_left, text_top))

        image_height = gold_icon_width
        tile_top = self.top + (self.height / 10) * 8.7
        tile_center_left = (
            self.left + self.width / 2 + (price_text_width / 2 - gold_icon_width / 2)
        )

        scaled_image = pygame.transform.smoothscale(
            SPRITES["coin"], (gold_icon_width, image_height)
        )

        self.canvas.blit(scaled_image, (tile_center_left, tile_top))

    def adjust_dimensions(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def on_click(self, mouse_button):
        if mouse_button[0]:
            print(f"Clicked on {self.card_info.name} : {str(type(self.card_info))}")
            if self.game_handler.buy_shop_item(self.card_info):
                print(
                    f"new player unit stash: {self.game_handler.get_current_player().units}"
                )
            else:
                print(
                    "Could not buy unit (possible reasons: not enough money / not gearup phase / max inventory size reached)"
                )
        elif mouse_button[2]:
            self.flipped = not self.flipped

