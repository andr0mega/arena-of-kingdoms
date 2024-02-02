class Unit:

    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def set_coordinates(self, coordinates):
        self.coordinates = coordinates