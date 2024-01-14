import pygame
from const.colors import *

class Shop:
    def __init__(self, canvas):
        self.canvas = canvas
        self.margin_left = 50
        self.margin_top = 50
        self.margin_right = 50
        self.margin_bottom = 50
        _, _, self.width_canvas, self.height_canvas = canvas.get_rect()

        self.shop_height = self.height_canvas - self.margin_top - self.margin_bottom
        self.shop_width = self.shop_height

        self.icon_width = 150
        self.icon_height = 60
        self.icon_top = self.margin_top
        self.icon_left = self.width_canvas - self.margin_right - self.icon_width

        self.font = pygame.font.SysFont("Rockwell", 38)
        self.isopen = False
        self.hover = False

    def get_color(self):
        if self.hover:
            return COLOR_SHOP_ICON_HOVER

        return COLOR_SHOP_ICON

    def draw_shop_icon(self):
        if self.isopen:
            render_text = self.font.render("Back", True, COLOR_SHOP_TEXT)
        else:
            render_text = self.font.render("Shop", True, COLOR_SHOP_TEXT)
        text_left = self.icon_left + (self.icon_width - render_text.get_width()) / 2
        text_top = self.icon_top + (self.icon_height - render_text.get_rect()[3]) / 2
        shop_icon_rect = pygame.rect.Rect(self.icon_left, self.icon_top, self.icon_width, self.icon_height)
        pygame.draw.rect(self.canvas, self.get_color(), shop_icon_rect, border_radius=20)
        self.canvas.blit(render_text, (text_left, text_top))
    
    def draw_shop(self):
        shop_background_rect = pygame.rect.Rect(self.margin_left - 2, self.margin_top - 2, self.shop_height + 4, self.shop_width + 4)
        shop_rect = pygame.rect.Rect(self.margin_left, self.margin_top, self.shop_height, self.shop_width)
        pygame.draw.rect(self.canvas, COLOR_SHOP_BACKGROUND, shop_background_rect)
        pygame.draw.rect(self.canvas, COLOR_SHOP, shop_rect)
        

    def shop_selected(self, left, top):
        mouse_shop_left = left - self.icon_left
        shop_right = self.icon_left + self.icon_width
        mouse_shop_top = top - self.icon_top
        shop_bottom = self.icon_top + self.icon_height
        if 0 < mouse_shop_left < shop_right and 0 < mouse_shop_top < shop_bottom:
            return True
        return False

    def open_shop(self):
        self.isopen = True
    
    def close_shop(self):
        self.isopen = False

    def set_hover(self, hover):
        self.hover = hover