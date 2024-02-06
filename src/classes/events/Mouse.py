import pygame

from classes.Tile import Tile


class Mouse:
    def __init__(self, elements):
        self.elements = elements
        self.last_tile = None

    def on_mouse_motion(self):
        pos = pygame.mouse.get_pos()

        for element in self.elements:
            element.on_hover(False)

            if hasattr(element, 'screen_rect') and element.screen_rect is not None:
                if element.screen_rect.collidepoint(pos):
                    element.on_hover(True)
                    if isinstance(element, Tile):
                        self.__on_tile_hover(element)



    def on_mouse_buttondown(self):
        pos = pygame.mouse.get_pos()

        for element in self.elements:
            if hasattr(element, 'screen_rect') and element.screen_rect is not None:
                if element.screen_rect.collidepoint(pos):
                    element.on_click()

    def __on_tile_hover(self, tile):
        if(self.last_tile != tile):
            for element in self.elements:
                tile_hover_changed = getattr(element, "on_tile_hover", None)
                if callable(tile_hover_changed):
                    tile_hover_changed(tile.tile_pos)
            pass
