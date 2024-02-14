import pygame
from classes.Tile import Tile

class EventHandler:
    _instance = None

    def __init__(self):
        self.reset_handler()
    
    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            print("EventHandler Instantiated")
            cls._instance = EventHandler()
        return cls._instance

    def reset_handler(self):
        self.selected_unit_tile = None
        self.last_tile = None
        self.on_clear_selected_tile_subscriber = []

    def set_elements(self, elements):
        self.elements = elements

    def subscribe_clear_selected_tile(self, subscriber):
        self.on_clear_selected_tile_subscriber.append(subscriber)

    def __notify_clear_selected_tile(self):
        for subscriber in self.on_clear_selected_tile_subscriber:
            try:
                subscriber.on_selected_tile_clear()
            except:
                print(f"on_selected_tile_clear not implemented by subscriber type: {str(type(subscriber))}")
            

    def on_mouse_motion(self):
        pos = pygame.mouse.get_pos()
        self.__off_tile_hover()

        for element in self.elements:
            element.on_hover(False)

            if hasattr(element, "screen_rect") and element.screen_rect is not None:
                if element.screen_rect.collidepoint(pos):
                    element.on_hover(True)
                    if isinstance(element, Tile):
                        self.__on_tile_hover(element)
                        

    def on_mouse_buttondown(self):
        pos = pygame.mouse.get_pos()
        click_elements = []
        tile_clicked = False
        for element in self.elements:
            if hasattr(element, "screen_rect") and element.screen_rect is not None:
                if element.screen_rect.collidepoint(pos):
                    click_elements.append(element)
                    tile_clicked = tile_clicked or isinstance(element, Tile)
        if(not tile_clicked and self.selected_unit_tile != None):
            self.selected_unit_tile = None
            self.__notify_clear_selected_tile()
        for element in click_elements:
            element.on_click()
    
    def set_unit_tile(self, tile):
        self.selected_unit_tile

    def __on_tile_hover(self, tile):
        if self.last_tile != tile:
            for element in self.elements:
                tile_hover_changed = getattr(element, "on_tile_hover", None)
                if callable(tile_hover_changed):
                    tile_hover_changed(tile.tile_pos)

    def __off_tile_hover(self):
        for element in self.elements:
            tile_hover_changed = getattr(element, "off_tile_hover", None)
            if callable(tile_hover_changed):
                tile_hover_changed()
