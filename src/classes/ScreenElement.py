import pygame
from const.colors import *


class ScreenElement:
    def __init__(self, canvas, color, margin_left=50, margin_top=50, margin_right=50, margin_bottom=50, hoverable=False):
        self.canvas = canvas

        self.margin_left = margin_left
        self.margin_top = margin_top
        self.margin_right = margin_right
        self.margin_bottom = margin_bottom
        self.hoverable = hoverable

        self.color = color

        self.hover = False

        _, _, self.width_canvas, self.height_canvas = self.canvas.get_rect()

        self.set_dimensions()

    def get_canvas_dimensions(self):
        _, _, self.width_canvas, self.height_canvas = self.canvas.get_rect()
        return (self.width_canvas, self.height_canvas)

    def set_dimensions(self):
        raise NotImplementedError("set_dimensions() must be implemented")

    def draw_self(self):
        self.set_dimensions()

        screen_rect = pygame.rect.Rect(
            self.left, self.top, self.width, self.height)
        pygame.draw.rect(self.canvas, self.color, screen_rect)

    def self_selected(self, mouse_left, mouse_top):
        if self.left < mouse_left < self.left + self.width and self.top < mouse_top < self.top + self.height:
            return True
        return False

    def set_color(self, color):
        self.color = color

    def set_hover(self, hover):
        self.hover = hover

    def get_color(self):
        if self.hover and not self.hoverable:
            return self.get_hover_color(self.color)

        return self.color

    def get_hover_color(color_tuple):
        return tuple(color - 25 for color in color_tuple)
