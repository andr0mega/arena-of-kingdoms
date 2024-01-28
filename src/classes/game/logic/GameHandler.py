from const.params import *
from GameBoard import *

class GameHandler:
    instance = None
    
    @staticmethod
    def get_instance():
        if(GameHandler.instance == None):
             instance = GameHandler()
        return instance
    
    def create_board(self, width, height):
        self.board = GameBoard(width, height)

    def load_config(self, )