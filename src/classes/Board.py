import pygame
from classes.ScreenElement import ScreenElement
from classes.Tile import Tile
from classes.game.logic.GameBoard import GameCoordinate
from classes.game.logic.GameHandler import GameHandler, GamePhase
from const.colors import *
import const.globals as globals


class Board(ScreenElement):
    def __init__(self, canvas, width=16):
        self.tile_rows = width
        self.tile_columns = width

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

    def on_tile_click(self, tile):
        gameHandler = GameHandler.get_instance()
        if gameHandler.phase == GamePhase.DEPLOYMENT:
            gameHandler.place_king(GameCoordinate(tile[0], tile[1]))
        elif gameHandler.phase == GamePhase.COMBAT:
            moveFields = gameHandler.get_possible_moves(
                GameCoordinate(tile[0], tile[1])
            )
            print(moveFields)

        self.__update_tiles()
        """
        if globals.phase == "deployment" and not globals.deployment_lock:
            tiles_to_deploy = []
            for i in range(max(tile[0] - 1, 0), min(tile[0] + 2, self.tile_columns)):
                for j in range(max(tile[1] - 1, 0), min(tile[1] + 2, self.tile_columns)):
                    if self.board[i][j].player == None:
                        tiles_to_deploy.append(self.board[i][j])
                    
            if len(tiles_to_deploy) == 9:
                for tile_deploy in tiles_to_deploy:
                    tile_deploy.set_player(globals.active_player)
                self.board[tile[0]][tile[1]].set_unit(globals.active_player.units["king"])
                globals.deployment_lock = True
        """

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

    def on_click(self):
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
