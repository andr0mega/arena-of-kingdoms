class Player:
    def __init__(self, name, nr, color):
        self.name = name
        self.color = color
        self.nr = nr
        self.active = False

    def enable(self):
        self.active = True
    
    def disable(self):
        self.active = False