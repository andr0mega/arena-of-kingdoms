import pygame

class Mouse:
    def __init__(self, board, shop, player):
        self.board = board
        self.player = player
        self.shop = shop

    def on_mouse_event(self):
        left, top = pygame.mouse.get_pos()

        shop_selected = self.shop.shop_selected(left, top)
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
                elif selected_tile != (None, None):
                    self.board.claim_tile(selected_tile[0], selected_tile[1], self.player)

            self.board.draw_board()
        self.shop.draw_shop_icon()
