import pygame
from classes.ScreenElement import ScreenElement
from const.colors import *
from const.params import *
import const.globals as globals


class PlayerInfoboxBorder(ScreenElement):
    def __init__(self, canvas):
        super().__init__(canvas, COLOR_PLAYER_INFOBOX_BORDER, hoverable=False)

    def set_dimensions(self):
        _ , height_canvas = super().get_canvas_dimensions()

        self.width = PLAYER_INFO_BOX_WIDTH + 2 * RECT_BORDER
        self.height = PLAYER_INFO_BOX_HEIGHT + 2 * RECT_BORDER
        self.top = self.margin_top - RECT_BORDER
        self.left = height_canvas - RECT_BORDER

    def draw_self(self):
        super().draw_self()

    def on_click(self):
        pass

class PlayerInfobox(ScreenElement):
    def __init__(self, canvas, players):
        super().__init__(canvas, COLOR_PLAYER_INFOBOX, hoverable=False)
        self.players = players

        self.font = pygame.font.SysFont("Rockwell", 18)

    def set_dimensions(self):
        _ , height_canvas = super().get_canvas_dimensions()

        self.width = PLAYER_INFO_BOX_WIDTH
        self.height = PLAYER_INFO_BOX_HEIGHT
        self.top = self.margin_top
        self.left = height_canvas

    def draw_self(self):
        super().draw_self()

        text = [f'Turn:  {globals.turn}',
                f'Phase:  {globals.phase.capitalize()}',
                f' ',
                f'Current Player:  {globals.active_player.name}',
                f'Balance:  {globals.active_player.balance}',
                f'Tiles:  {globals.active_player.get_tile_amount()}',
                f'Income:  TODO']
        
        line_break = 0
        for line in text:
            render_line = self.font.render(line, True, COLOR_PLAYER_INFOBOX_TEXT)
            line_left = self.left + 5
            line_top = self.top + 5 + line_break
            line_break += render_line.get_rect()[3] + 2
            self.canvas.blit(render_line, (line_left, line_top))

    def get_color(self):
        return globals.active_player.color

    def on_click(self):
        pass

class TileInfoboxBorder(ScreenElement):
    def __init__(self, canvas):
        super().__init__(canvas, COLOR_TILE_INFOBOX_BORDER, hoverable=False)

    def set_dimensions(self):
        _ , height_canvas = super().get_canvas_dimensions()

        self.width = TILE_INFO_BOX_WIDTH + 2 * RECT_BORDER
        self.height = TILE_INFO_BOX_HEIGHT + 2 * RECT_BORDER
        self.top = self.margin_top + PLAYER_INFO_BOX_HEIGHT + SPACING_INFO_BOXES_HEIGHT - RECT_BORDER
        self.left = height_canvas - RECT_BORDER

    def draw_self(self):
        super().draw_self()

    def on_click(self):
        pass


class TileInfobox(ScreenElement):
    def __init__(self, canvas):
        super().__init__(canvas, COLOR_TILE_INFOBOX, hoverable=False)

        self.font = pygame.font.SysFont("Rockwell", 18)

    def set_dimensions(self):
        _ , height_canvas = super().get_canvas_dimensions()

        self.width = TILE_INFO_BOX_WIDTH
        self.height = TILE_INFO_BOX_HEIGHT
        self.top = self.margin_top + PLAYER_INFO_BOX_HEIGHT + SPACING_INFO_BOXES_HEIGHT
        self.left = height_canvas

    def draw_self(self):
        super().draw_self()

        text = [f'Tile owner: ',
                f'Ipsum',
                f'Dolor',
                f'Sit',
                f'Amet',
                f'Hello World']
        
        line_break = 0
        for line in text:
            render_line = self.font.render(line, True, COLOR_TILE_INFOBOX_TEXT)
            line_left = self.left + 5
            line_top = self.top + 5 + line_break
            line_break += render_line.get_rect()[3] + 2
            self.canvas.blit(render_line, (line_left, line_top))

    def on_click(self):
        pass