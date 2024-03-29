import pygame
from classes.ScreenElement import ScreenElement
from classes.events.EventHandler import EventHandler
from classes.Tile import Tile
from classes.game.logic.GameBoard import GameCoordinate
from classes.game.logic.GameHandler import GameHandler, GamePhase
from const.colors import *


class Board(ScreenElement):
    def __init__(self, canvas, width):
        self.tile_rows = width
        self.tile_columns = width
        self.game_handler = GameHandler.get_instance()
        self.event_handler = EventHandler.get_instance()

        super().__init__(canvas, COLOR_BOARD_BACKGROUND)

        def create_tile(column, row):
            tile = Tile(
                canvas,
                left=self.margin_left + column * self.tile_width,
                top=self.margin_top + row * self.tile_width,
                width=self.tile_width,
                height=self.tile_width,
                on_tile_click=self.on_tile_click,
                tile_pos=(column, row),
                board=self,
            )
            return tile

        self.is_visible = True

        self.board = [
            [create_tile(column, row) for row in range(self.tile_rows)]
            for column in range(self.tile_rows)
        ]
        self.event_handler.subscribe_clear_selected_tile(self)

    def on_tile_click(self, tile):
        if self.game_handler.phase == GamePhase.DEPLOYMENT:
            self.game_handler.place_king(GameCoordinate(tile[0], tile[1]))
        elif self.game_handler.phase == GamePhase.COMBAT:
            moveFields = self.game_handler.get_possible_moves(
                GameCoordinate(tile[0], tile[1])
            )
            attackFields = self.game_handler.get_possible_attacks(
                GameCoordinate(tile[0], tile[1])
            )
            if moveFields != None or attackFields != None:
                self.event_handler.clear_selected_tile()
                for pMove in moveFields:
                    guiTile = self.board[pMove[0]][pMove[1]]
                    guiTile.set_movable(True)
                for pAttack in attackFields:
                    guiTile = self.board[pAttack[0]][pAttack[1]]
                    guiTile.set_attackable(True)
                self.event_handler.selected_unit_tile = tuple([tile[0], tile[1]])
            elif self.event_handler.selected_unit_tile != None:
                # field is selected, check if move / attack field is selected, or clear moveable field
                self.__combat_action_on_tile(tuple([tile[0], tile[1]]))

        self.__update_tiles()

    def __combat_action_on_tile(self, action_tile):
        # field is selected, check if move / attack field is selected, or clear moveable field
        selectedUnitTile = self.event_handler.selected_unit_tile
        if action_tile in self.game_handler.get_possible_moves(
            GameCoordinate(selectedUnitTile[0], selectedUnitTile[1])
        ):
            self.game_handler.move_unit(
                GameCoordinate(selectedUnitTile[0], selectedUnitTile[1]),
                GameCoordinate(action_tile[0], action_tile[1]),
            )
            self.event_handler.clear_selected_tile()
        elif (action_tile in self.game_handler.get_possible_attacks(
            GameCoordinate(selectedUnitTile[0], selectedUnitTile[1])
        )):
            self.game_handler.attack_unit(
                GameCoordinate(selectedUnitTile[0], selectedUnitTile[1]),
                GameCoordinate(action_tile[0], action_tile[1]),
            )
            self.event_handler.clear_selected_tile()
        self.__update_tiles()

    def on_selected_tile_clear(self):
        for row in self.board:
            for tile in row:
                tile.set_attackable(False)
                tile.set_placeable(False)
                tile.set_movable(False)
                pass

    def __update_tiles(self):
        gameHandler = GameHandler.get_instance()
        gameField = gameHandler.board.fields
        for x in range(self.tile_columns):
            for y in range(self.tile_rows):
                guiTile = self.board[x][y]
                gameTile = gameField[x][y]
                guiTile.set_player(gameTile.owner)
                guiTile.set_unit(gameTile.troop)
                guiTile.set_building(gameTile.building)

    def on_click(self, mouse_button):
        pass

    def get_tiles(self):
        tiles = []
        for column in self.board:
            for tile in column:
                tiles.append(tile)
        return tiles

    def set_dimensions(self):
        _, height_canvas = super().get_canvas_dimensions()
        base_height = height_canvas - self.margin_top - self.margin_bottom
        base_width = base_height
        self.tile_width = int(base_width / self.tile_rows)
        self.tile_height = int(base_height / self.tile_columns)

        self.left = self.margin_left
        self.top = self.margin_top

        self.width = self.tile_width * self.tile_rows + 1
        self.height = self.tile_height * self.tile_columns + 1

    def set_visibility(self, visibility):
        self.is_visible = visibility

    def get_tiles_for_player(self, player):
        tile_amount = 0
        for tile in self.get_tiles():
            if tile.player == player:
                tile_amount += 1
        return tile_amount

    def draw_self(self):

        if not self.is_visible:
            return

        super().draw_self()

        for column in range(len(self.board)):
            for row in range(len(self.board[column])):
                current_tile = self.board[column][row]
                current_tile.adjust_dimensions(
                    self.margin_left + column * self.tile_width,
                    self.margin_top + row * self.tile_height,
                    self.tile_width,
                    self.tile_height,
                )
