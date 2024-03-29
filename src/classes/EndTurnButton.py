import pygame
from classes.ScreenElement import ScreenElement
from const.colors import *
from const.params import *


class EndTurnButton(ScreenElement):
    def __init__(self, canvas, on_click_callback):
        super().__init__(canvas, COLOR_END_TURN_ICON, hoverable=True)

        self.font = pygame.font.SysFont("Rockwell", 28)
        self.border_radius = 18

        self.on_click_callback = on_click_callback

    def set_dimensions(self):
        width_canvas, height_canvas = super().get_canvas_dimensions()

        self.width = END_TURN_BUTTON_WIDTH
        self.height = END_TURN_BUTTON_HEIGHT
        self.top = height_canvas - self.margin_bottom - self.height
        self.left = width_canvas - self.margin_right - self.width

    def draw_self(self):
        super().draw_self()
        text = "End turn"

        render_text = self.font.render(text, True, COLOR_END_TURN_TEXT)
        text_left = self.left + (self.width - render_text.get_width()) / 2
        text_top = self.top + (self.height - render_text.get_rect()[3]) / 2
        self.canvas.blit(render_text, (text_left, text_top))

    def on_click(self, mouse_button):
        if mouse_button[0]:
            self.on_click_callback()
