import pygame
from const.colors import *

class Tile(pygame.rect.Rect):
    def __init__(self, left, top, width, height): 
        self.left = left +1
        self.top = top +1
        self.width = width -2
        self.height = height -2
        self.player = None
        self.hover = False
        super(Tile, self).__init__(self.left, self.top, self.width, self.height)

    def draw_self(self, canvas):
        pygame.draw.rect(canvas, self.get_color(), self)

    def get_color(self):
        if self.hover:
            if not self.player:
                return COLOR_NEUTRAL_TILE_HOVER
            else:
                return COLOR_PLAYER1_HOVER
            
        if self.player:
            return self.player.color
        
        return COLOR_NEUTRAL_TILE
    
    def set_player(self, player):
        self.player = player

    def set_hover(self, hover):
        self.hover = hover