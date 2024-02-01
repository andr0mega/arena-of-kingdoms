from enum import Enum
from classes.game.config.GameConfig import GameConfig
from const.params import *
from GameBoard import *
from GamePlayer import GamePlayer
from GameValidator import valid_king_position
import random

#Singleton GameHandler
class GameHandler:
    instance = None

    @staticmethod
    def get_instance():
        if(GameHandler.instance == None):
             instance = GameHandler()
             instance.clear_handler()
        return instance
    
    def clear_handler(self):
        self.board = None
        self.game_config = None
        self.players = []
        self.player_order = []
        self.game_state = GameState.NONE
        self.current_player_index = 0
        self.action_log = []

    def create_board(self, width: int, height: int):
        self.board = GameBoard(width, height)

    def set_config(self, game_config: GameConfig):
        self.game_config = game_config

    def register_player(self, name, color):
        #create player with increasing number
        GamePlayer(len(self.players)+1, name, color, START_BALANCE)

    def get_game_state(self):
        return self.game_state

    #returns current player or None, if the game hasen't started
    def get_current_player(self) -> GamePlayer:
        return self.players[self.player_order[self.current_player_index]]

    def start_game(self) -> bool:
        if(not self.is_game_ready()):
            return False
        self.player_order = [i for i in range(self.players)]
        random.shuffle(self.player_order)
        self.current_player_index = 0
        self.game_state = GameState.RUNNING
        return True
    
    def set_king(self, coordinates: GameCoordinate) -> bool:
        if(not valid_king_position(self, coordinates)):
            return False
        #Missing method: create Troop from config
        player = self.get_current_player()

    def is_game_ready(self) -> bool:
        if(self.game_state != GameState.NONE or len(self.players) < 2):
            return False
        return self.board != None and self.game_config != None
    
    



class GameState(Enum):
    NONE = 1
    RUNNING = 2
    FINISHED = 3