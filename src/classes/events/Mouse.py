import pygame


class Mouse:
    def __init__(self, elements):
        self.elements = elements
        self.mouse_pressed = False

    def on_mouse_event(self):
        pos = pygame.mouse.get_pos()

        for element in self.elements:
            element.on_hover(False)

            if hasattr(element, 'screen_rect'):
                if element.screen_rect.collidepoint(pos):
                    element.on_hover(True)

                    if pygame.mouse.get_pressed()[0]:
                        if (self.mouse_pressed == False):
                            self.mouse_pressed = True
                    else:
                        if (self.mouse_pressed == True):
                            element.on_click()
                        self.mouse_pressed = False

        # else:
        #     hovered_tile = self.board.get_tile(left, top)
        #     if hovered_tile != (None, None):
        #         self.board.hover_tile(hovered_tile[0], hovered_tile[1])
        #     else:
        #         self.board.reset_hover()

        #     if pygame.mouse.get_pressed()[0]:
        #         selected_tile = self.board.get_tile(left, top)
        #         if shop_selected:
        #             self.shop.open_shop()
        #         #elif end_turn_selected:
        #         #    self.screen.set_end_turn(True)
        #         elif selected_tile != (None, None):
        #             self.board.claim_tile(selected_tile[0], selected_tile[1])

        #     self.board.draw_self()
        # self.shop.draw_shop_icon()
        # self.screen.draw_end_turn_icon()
