import pygame

class Mouse:
    def __init__(self, board, shop):
        self.board = board
        self.shop = shop

    def on_mouse_event(self):
        left, top = pygame.mouse.get_pos()

        shop_selected = self.shop.self_selected(left, top)
        #end_turn_selected = self.screen.end_turn_selected(left, top)

        #if end_turn_selected:
        #    self.screen.set_end_turn_hover(True)
        #else:
        #    self.screen.set_end_turn_hover(False)
        
        if shop_selected:
            self.shop.set_hover(True)
        else:
            self.shop.set_hover(False)

        if self.shop.isopen:
            self.shop.draw_shop()
            if pygame.mouse.get_pressed()[0]:
                if shop_selected:
                    self.shop.close_shop()
        else:
            hovered_tile = self.board.get_tile(left, top)
            if hovered_tile != (None, None):
                self.board.hover_tile(hovered_tile[0], hovered_tile[1])
            else:
                self.board.reset_hover()
                
            if pygame.mouse.get_pressed()[0]:
                selected_tile = self.board.get_tile(left, top)
                if shop_selected:
                    self.shop.open_shop()
                #elif end_turn_selected:
                #    self.screen.set_end_turn(True)
                elif selected_tile != (None, None):
                    self.board.claim_tile(selected_tile[0], selected_tile[1])

            self.board.draw_board()
        #self.shop.draw_shop_icon()
        #self.screen.draw_end_turn_icon()
