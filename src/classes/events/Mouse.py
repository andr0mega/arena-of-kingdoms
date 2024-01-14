import pygame

class Mouse:
    def __init__(self, board, player):
        self.board = board
        self.player = player

    def on_mouse_event(self):
        left, top = pygame.mouse.get_pos()
        hovered_tile = self.board.get_tile(left, top)
        if hovered_tile != (None, None):
            self.board.hover_tile(hovered_tile[0], hovered_tile[1])
        else:
            self.board.reset_hover()
        
        if pygame.mouse.get_pressed()[0]:
            selected_tile = self.board.get_tile(left, top)
            if selected_tile != (None, None):
                self.board.claim_tile(selected_tile[0], selected_tile[1], self.player)
        
        self.board.draw_board()
