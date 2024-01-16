import pygame
from const.colors import *
from helpers import get_hover_color

class Screen:
    def __init__(self, canvas):
        self.canvas = canvas
        self.margin_left = 50
        self.margin_top = 50
        self.margin_right = 50
        self.margin_bottom = 50

        self.end_turn_icon_width = 150
        self.end_turn_icon_height = 50

        self.set_end_turn_dimensions()

        self.font = pygame.font.SysFont("Rockwell", 28)
        self.end_turn_hover = False
        self.end_turn = False

    def set_end_turn_dimensions(self):
        _, _, self.width_canvas, self.height_canvas = self.canvas.get_rect()
        self.end_turn_icon_top = self.height_canvas - self.margin_bottom - self.end_turn_icon_height
        self.end_turn_icon_left = self.width_canvas - self.margin_right - self.end_turn_icon_width

    def get_color(self):
        if self.end_turn_hover:
            return get_hover_color(COLOR_END_TURN_ICON)

        return COLOR_END_TURN_ICON

    def draw_end_turn_icon(self):
        self.set_end_turn_dimensions()

        end_turn_icon_text = "End turn"

        render_text = self.font.render(end_turn_icon_text, True, COLOR_END_TURN_TEXT)
        text_left = self.end_turn_icon_left + (self.end_turn_icon_width - render_text.get_width()) / 2
        text_top = self.end_turn_icon_top + (self.end_turn_icon_height - render_text.get_rect()[3]) / 2
        end_turn_icon_rect = pygame.rect.Rect(self.end_turn_icon_left, self.end_turn_icon_top, self.end_turn_icon_width, self.end_turn_icon_height)
        pygame.draw.rect(self.canvas, self.get_color(), end_turn_icon_rect, border_radius=15)
        self.canvas.blit(render_text, (text_left, text_top))
    
    def end_turn_selected(self, left, top):
        mouse_end_turn_left = left - self.end_turn_icon_left
        end_turn_icon_right = self.end_turn_icon_width
        mouse_end_turn_top = top - self.end_turn_icon_top
        end_turn_icon_bottom = self.end_turn_icon_height
        if 0 < mouse_end_turn_left < end_turn_icon_right and 0 < mouse_end_turn_top < end_turn_icon_bottom:
            return True
        return False    

    def set_end_turn(self, bool):
        self.end_turn = bool
        print("turn ended")
    
    def set_end_turn_hover(self, hover):
        self.end_turn_hover = hover 



