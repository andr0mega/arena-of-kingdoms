import pygame


class Mouse:
    def __init__(self, elements):
        self.elements = elements

    def on_mouse_motion(self):
        pos = pygame.mouse.get_pos()

        for element in self.elements:
            element.on_hover(False)

            if hasattr(element, 'screen_rect') and element.screen_rect is not None:
                if element.screen_rect.collidepoint(pos):
                    element.on_hover(True)


    def on_mouse_buttondown(self):
        pos = pygame.mouse.get_pos()

        for element in self.elements:
            if hasattr(element, 'screen_rect') and element.screen_rect is not None:
                if element.screen_rect.collidepoint(pos):
                    element.on_click()

