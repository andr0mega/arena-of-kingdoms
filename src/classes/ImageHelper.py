from classes.game.config.TroopConfig import TroopConfig
from classes.game.config.BuildingConfig import BuildingConfig
from const.sprites import SPRITES

def get_image_for_troop(troopName: str):
    return SPRITES[troopName]

def get_image_for_building(buildingName: str):
    return SPRITES[buildingName]