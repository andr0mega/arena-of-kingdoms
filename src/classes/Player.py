class Player:
    def __init__(self, name, nr, color):
        self.name = name
        self.color = color
        self.nr = nr
        self.active = False

    def toggle_active(self, active):
        self.active = active

