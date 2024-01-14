from uuid import uuid4

class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.id = uuid4()