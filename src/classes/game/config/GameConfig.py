from const.params import *
from TroopConfig import *
import json

class GameConfig:

    def __init__(self):
        self.board_settings = json.loads(GAME_SETTINGS)
        self.king_settings = json.loads(KING)
        troops = json.loads(TROOPS)
        self.troops = [TroopConfig(troop.display_name,
                     troop.name,
                     troop.cost,
                     troop.health,
                     troop.offense,
                     troop.defense,
                     troop.speed,
                     troop.upkeep) for troop in troops]

    #Returns first found config of troop name (if none found returns None)
    def get_troop_config(self, troopName):
        return next(troop for troop in self.troops if troop.name == troopName)