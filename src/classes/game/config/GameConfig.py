from classes.game.config.BuildingConfig import BuildingConfig
from const.params import *
from classes.game.config.TroopConfig import TroopConfig
import json

class GameConfig:

    def __init__(self):
        self.board_settings = json.loads(GAME_SETTINGS)
        king_param = json.loads(KING)
        troops = json.loads(TROOPS)
        buildings = json.loads(BUILDINGS)
        self.king_config = TroopConfig(king_param["display_name"],
                     king_param["name"],
                     king_param["cost"],
                     king_param["health"],
                     king_param["offense"],
                     king_param["defense"],
                     king_param["speed"],
                     king_param["upkeep"],
                     "")
        self.troops = [TroopConfig(troop["display_name"],
                     troop["name"],
                     troop["cost"],
                     troop["health"],
                     troop["offense"],
                     troop["defense"],
                     troop["speed"],
                     troop["upkeep"],
                     troop["description"]) for troop in troops]

        self.buildings = [BuildingConfig(building["display_name"],
                     building["name"],
                     building["cost"],
                     building["health"],
                     building["blocking"],
                     building["production"],
                     building["description"]) for building in buildings]

    #Returns first found config of troop name (if none found returns None)
    def get_troop_config(self, troopName):
        if(self.king_config.name == troopName):
            return self.king_config
        return next(iter([troop for troop in self.troops if troop.name == troopName]), None)