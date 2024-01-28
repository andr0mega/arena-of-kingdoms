class Field:    
    def __init__(self, owner, unit, building):
        self.owner = owner
        self.unit = unit
        self.building = building


    @staticmethod
    def builder():
        return Field.Builder()

    class Builder:
        def __init__(self):
            self.owner = None
            self.unit = None
            self.building = None

        def set_owner(self, owner):
            self.owner = owner

        def set_unit(self, unit):
            self.unit = unit

        def set_building(self, building):
            self.building = building
        
        def build(self):
            return Field(self.owner, self.unit, self.building)
