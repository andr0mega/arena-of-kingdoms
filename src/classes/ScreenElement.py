import pygame
from const.colors import *
from const.params import *


class ScreenElement:
    def __init__(self, canvas, color, hoverable=False):
        self.canvas = canvas

        self.margin_left = MARGIN_LEFT
        self.margin_top = MARGIN_TOP
        self.margin_right = MARGIN_RIGHT
        self.margin_bottom = MARGIN_BOTTOM
        self.border_radius = 0
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

    def on_click(self):
        print(f"{type(self).__name__} has no on_click method")

    def on_hover(self, hover):
        self.hover = hover

    def draw_self(self):
        self.set_dimensions()

        color = self.get_color()

        if self.hover and self.hoverable:
            color = self.get_hover_color(color)

        self.screen_rect = pygame.rect.Rect(
            self.left,
            self.top,
            self.width,
            self.height
        )
        pygame.draw.rect(
            self.canvas,
            color,
            self.screen_rect,
            border_radius=self.border_radius
        )

    def get_color(self):
        return self.color

    def get_hover_color(self, color_tuple):
        return tuple(color - 25 for color in color_tuple)
