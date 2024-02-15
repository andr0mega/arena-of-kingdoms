from enum import Enum
import re
from typing import Dict
from classes.game.config.TroopConfig import TroopConfig
from classes.game.config.BuildingConfig import BuildingConfig
from classes.game.logic.action.MoveAction import MoveAction
from classes.game.logic.action.BuyAction import BuyAction
from classes.game.config.GameConfig import GameConfig
from classes.game.logic.unit.Troop import Troop
from const.params import *
from classes.game.logic.GameBoard import GameBoard
from classes.game.logic.GameBoard import GameCoordinate
from classes.game.logic.GamePlayer import GamePlayer
from classes.game.config.UnitConfig import UnitConfig
from classes.game.logic.GameValidator import (
    is_valid_turn,
    possible_move_positions,
    valid_king_position,
)
from classes.game.logic.action.PlaceAction import PlaceAction

import random

#!!!IMPORTANT Singleton GameHandler
"""
    process:
    clear_handler
        - create board
        - set config
        - register players
        - start game
        - set king
        - end turn
"""


class GameHandler:
    _instance = None

    def __init__(self):
        self.clear_handler()

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            print("GameHandler Instantiated")
            cls._instance = GameHandler()
        return cls._instance

    # Method clears handler ->
    def clear_handler(self):
        self.board = None
        self.game_config = None
        self.players = []
        self.player_order = []
        self.game_state = GameState.NONE
        self.current_player_index = 0
        self.round = 0
        # Deployment phase only exists in the 1st round
        self.phase = GamePhase.DEPLOYMENT
        # action_log contains the actions per round and per player. Key is a tuple of (round, phase, player_number)
        # The value of the log is a list with items of type GameAction
        self.action_log = {}

    # 1.
    def create_board(self, width: int, height: int):
        self.board = GameBoard(width, height)

    # 2.
    def set_config(self, game_config: GameConfig):
        self.game_config = game_config

    # 3.
    def register_player(self, name, color):
        # create player with increasing number
        self.players.append(
            GamePlayer(
                len(self.players) + 1,
                name,
                color,
                self.game_config.board_settings["start_balance"],
            )
        )

    # 4.
    def start_game(self) -> bool:
        print("GAME STARTED")
        if not self.__is_game_ready():
            return False
        self.player_order = [i for i in range(len(self.players))]
        random.shuffle(self.player_order)
        self.current_player_index = 0
        self.game_state = GameState.RUNNING
        return True

    # ---------------------------- DEPLOYMENT ACTIONS START -----------------------------

    # 5. Place King (Special placement, other troops can only be placed in fields already occupied by player)
    def place_king(self, coordinates: GameCoordinate) -> bool:
        # Can place king, if it is the first round and the game is running
        if (
            self.game_state != GameState.RUNNING
            or self.round != 0
            or self.phase != GamePhase.DEPLOYMENT
            or not valid_king_position(self, coordinates)
        ):
            return False
        # Create King troop and set on field.
        player = self.get_current_player()
        # King is already assigned to the player (must have been placed already)
        if len(player.get_units_of_type("king")) > 0:
            return False
        king = self.game_config.get_troop_config("king").create_from_config()
        player.add_unit(king)
        self.board.fields[coordinates.x][coordinates.y].troop = king
        for x in range(coordinates.x - 1, coordinates.x + 2):
            for y in range(coordinates.y - 1, coordinates.y + 2):
                self.board.fields[x][y].owner = player
        self.__get_current_action_log().append(PlaceAction(coordinates, king))
        return True
    # ---------------------------- DEPLOYMENT ACTIONS END ------------------------------

    # ---------------------------- GEARUP ACTIONS START ------------------------------
    def buy_shop_item(self, unitConfig: UnitConfig):
        player = self.get_current_player()
        if(self.phase == GamePhase.GEARUP):
            if(player.balance >= unitConfig.cost):
                newUnit = unitConfig.create_from_config()
                player.add_unit(newUnit)
                player.reduce_balance(unitConfig.cost)
                self.__get_current_action_log().append(BuyAction(newUnit))
                return True
        return False
    
    # ---------------------------- GEARUP ACTIONS END ------------------------------

    # ------------------------------- COMBAT ACTIONS START -----------------------------

    def move_unit(self, coordinates_from:GameCoordinate, coordinates_to:GameCoordinate):
        
        moveToTuple = tuple([coordinates_to.x,coordinates_to.y])
        possible_fields = self.get_possible_moves(coordinates_from)
        if(possible_fields != None and moveToTuple in possible_fields):
            moveFieldFrom = self.board.fields[coordinates_from.x][coordinates_from.y]
            moveFieldTo = self.board.fields[coordinates_to.x][coordinates_to.y]
            if(moveFieldFrom.troop != None and moveFieldFrom.troop in self.get_current_player().units):
                moveAction = MoveAction(moveFieldFrom.troop, coordinates_from, coordinates_to, GameBoard.calculate_distance(coordinates_from, coordinates_to))
                moveFieldTo.troop = moveFieldFrom.troop
                moveFieldFrom.troop = None
                #if troop is claiming field (maybe some will not claim fields)
                moveFieldTo.owner = self.get_current_player()
                self.__get_current_action_log().append(moveAction)
                return True
        return False

    def attack_unit(self, coordinates_from, coordinates_to):

        pass

    # ------------------------------- COMBAT ACTIONS END -------------------------------

    # End Turn of the current player. ()
    def end_turn(self) -> bool:
        if is_valid_turn(self):
            self.current_player_index += 1
            if self.current_player_index == len(self.player_order):
                # turn-order is over, switch to new phase / round
                self.current_player_index = 0
                self.__end_phase()
            pass
        return False

    # returns possible move-fields for the troop on the field 
    # if there is a troop, and it belongs to the current player - None otherwise
    def get_possible_moves(self, coordinates) -> list:
        checkField = self.board.fields[coordinates.x][coordinates.y]
        moveTroop = checkField.troop
        if moveTroop != None and moveTroop in self.get_current_player().units:
            self.action_log
            remainingMovement = self.__current_remaning_move_dict()[moveTroop]
            return possible_move_positions(
                remainingMovement, self.board.fields, coordinates
            )
        return None


    # returns possible attack-fields for the troop on the field 
    # if there is a troop, and it belongs to the current player - None otherwise
    def get_possible_attacks(self, coordinates) -> list:
        print(f"possible attacks in handler: {str(coordinates)}")
        checkField = self.board.fields[coordinates.x][coordinates.y]
        moveTroop = checkField.troop
        if moveTroop != None and moveTroop in self.get_current_player().units:
            #TODO: get attackable tiles
            return []
        return None

    # returns current player or None, if the game hasen't started (TODO: check game status)
    def get_current_player(self) -> GamePlayer:
        return self.players[self.player_order[self.current_player_index]]

    def get_player_fields(self, player):
        player_fields = []
        for row in range(len(self.board.fields)):
            for column in range(len(self.board.fields[row])):
                if self.board.fields[row][column].owner == player:
                    player_fields.append(self.board.fields[row][column])
        return player_fields

    def get_game_state(self):
        return self.game_state

    def __current_remaning_move_dict(self) -> Dict:
        actionLog = self.__get_current_action_log()
        moveDict = {}
        for troop in [
            unit for unit in self.get_current_player().units if type(unit) == Troop
        ]:
            moveDict[troop] = troop.speed
        for action in actionLog:
            if type(action) == MoveAction:
                moveDict[action.troop] = moveDict[action.troop] - action.distance
        return moveDict

    def __end_phase(self):
        # Deployment is only part of round 1
        if self.phase == GamePhase.DEPLOYMENT:
            self.phase = GamePhase.GEARUP
        elif self.phase == GamePhase.GEARUP:
            self.phase = GamePhase.COMBAT
        elif self.phase == GamePhase.COMBAT:
            self.phase = GamePhase.INCOME
        elif self.phase == GamePhase.INCOME:
            self.phase = GamePhase.GEARUP
            self.round += 1

    def __is_game_ready(self) -> bool:
        if self.game_state != GameState.NONE or len(self.players) < 2:
            return False
        return self.board != None and self.game_config != None

    def __get_player_round_tuple(self) -> tuple:
        return tuple([self.round, self.phase, self.get_current_player().nr])

    def __get_current_action_log(self) -> list:
        logTuple = self.__get_player_round_tuple()
        if not logTuple in self.action_log:
            self.action_log[logTuple] = []
        return self.action_log[logTuple]


class GameState(Enum):
    NONE = 1
    RUNNING = 2
    FINISHED = 3


class GamePhase(Enum):
    DEPLOYMENT = "deployment"
    GEARUP = "gearup"
    COMBAT = "combat"
    INCOME = "income"
