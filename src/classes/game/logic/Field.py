from classes.game.logic.GamePlayer import GamePlayer
from classes.game.logic.unit.Building import Building
from classes.game.logic.unit.Troop import Troop


class Field:    
    def __init__(self, owner: GamePlayer, troop: Troop, building: Building):
        self.owner = owner
        self.troop = troop
        self.building = building


    @staticmethod
    def builder():
        return Field.Builder()

    class Builder:
        def __init__(self):
            self.owner = None
            self.troop = None
            self.building = None

        def set_owner(self, owner: GamePlayer):
            self.owner = owner

        def set_troop(self, troop: Troop):
            self.troop = troop

        def set_building(self, building: Building):
            self.building = building
        
        def build(self):
            return Field(self.owner, self.troop, self.building)
