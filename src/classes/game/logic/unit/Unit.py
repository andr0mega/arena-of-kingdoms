from GameBoard import GameCoordinate
class Unit:
    def get_name(self) -> str:
        return self.name

    def set_coordinates(self, coordinates: GameCoordinate):
        self.coordinates = coordinates