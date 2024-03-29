import pygame
from classes.game.config.TroopConfig import TroopConfig
from classes.game.config.BuildingConfig import BuildingConfig
from const.sprites import SPRITES
MOVEABLE = "move"
PLACEABLE = "place"
ATTACKABLE = "attack"


class ImageHelper:
    _instance = None

    def __init__(self):
        self.__init_image_storage()
    
    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            print("ImageHelper Instantiated")
            cls._instance = ImageHelper()
        return cls._instance
    

    def __init_image_storage(self):
        #holds the calculated images (key = tuple of name, width, height)
        self.image_storage_dict = {}
        
    def get_image_for_troop(self, troopName: str, width: int, height: int):

        return SPRITES[troopName]


    def get_image_for_building(self, buildingName: str):
        return SPRITES[buildingName]

    def get_image_possible_move(self, width: int, height: int):
        if not tuple([MOVEABLE,width,height]) in self.image_storage_dict:
            self.image_storage_dict[tuple([MOVEABLE,width,height])] = pygame.transform.smoothscale(SPRITES[MOVEABLE], (width, height))
        return self.image_storage_dict[tuple([MOVEABLE,width,height])]

    def get_image_possible_place(self, width: int, height: int):
        if not tuple([PLACEABLE,width,height]) in self.image_storage_dict:
            self.image_storage_dict[tuple([PLACEABLE,width,height])] = pygame.transform.smoothscale(SPRITES[PLACEABLE], (width, height))
        return self.image_storage_dict[tuple([PLACEABLE,width,height])]

    def get_image_possible_attack(self, width: int, height: int):
        if not tuple([ATTACKABLE,width,height]) in self.image_storage_dict:
            self.image_storage_dict[tuple([ATTACKABLE,width,height])] = pygame.transform.smoothscale(SPRITES[ATTACKABLE], (width, height))
        return self.image_storage_dict[tuple([ATTACKABLE,width,height])]
    
    
def get_image_for_troop(troopName: str):
    return SPRITES[troopName]


def get_image_for_building(buildingName: str):
    return SPRITES[buildingName]
