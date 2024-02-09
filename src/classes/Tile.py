import pygame
from classes.ScreenElement import ScreenElement
from classes.elements.Building import Building
from classes.game.logic.GamePlayer import GamePlayer
from classes.game.logic.unit.Troop import Troop
from const.colors import *
from classes.ImageHelper import get_image_for_troop
from classes.ImageHelper import ImageHelper
import const.globals as globals


class Tile(ScreenElement):
    def __init__(
        self, canvas, left, top, width, height, tile_pos, on_tile_click, board
    ):
        self.left = left + 1
        self.top = top + 1
        self.width = width - 1
        self.height = height - 1

        super().__init__(canvas, COLOR_NEUTRAL_TILE, hoverable=True)

        self.on_tile_click = on_tile_click
        self.tile_pos = tile_pos
        self.board = board
        self.player = None

        self.unit = None
        self.building = None
        self.moveable = False
        self.attackable = False
        self.placeable = False
        
        self.image_helper = ImageHelper.get_instance()

    def draw_self(self):
        if not self.board.is_visible:
            return

        super().draw_self()

        if self.unit != None:
            image_height = int(self.height * 0.75)
            image_width = int(self.width * 0.75)
            tile_center_top = self.top + self.height / 2 - image_height / 2
            tile_center_left = self.left + self.width / 2 - image_width / 2

            scaled_image = pygame.transform.smoothscale(
                get_image_for_troop(self.unit.name), (image_width, image_height)
            )

            self.canvas.blit(scaled_image, (tile_center_left, tile_center_top))
        image_height = int(self.height)
        image_width = int(self.width)
        if(self.moveable):
            self.draw_indication(self.image_helper.get_image_possible_move(image_width, image_height))
        elif(self.attackable):
            self.draw_indication(get_image_possible_attack())
        elif(self.placeable):
            self.draw_indication(get_image_possible_place())

    def draw_indication(self, scaled_image):
        image_height = int(self.height)
        image_width = int(self.width)
        tile_center_top = self.top + self.height / 2 - image_height / 2
        tile_center_left = self.left + self.width / 2 - image_width / 2
        self.canvas.blit(scaled_image, (tile_center_left, tile_center_top))
    
    def adjust_dimensions(self, left, top, width, height):
        self.left = left + 1
        self.top = top + 1
        self.width = width - 1
        self.height = height - 1

    def get_color(self):
        if self.player:
            return self.player.color

        return COLOR_NEUTRAL_TILE

    def set_dimensions(self):
        pass

    def set_movable(self, moveable: bool):
        self.moveable = moveable

    def set_placeable(self, placeable: bool):
        self.placeable = placeable
    
    def set_attackable(self, attackable: bool):
        self.attackable = attackable

    def set_player(self, player: GamePlayer):
        self.player = player

    def set_unit(self, unit: Troop):
        self.unit = unit

    def on_click(self):
        self.on_tile_click(self.tile_pos)

    def set_building(self, building):
        self.building = building
