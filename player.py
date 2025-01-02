class Player:
    def __init__(self, name, location, is_spy=False):
        self.name = name
        self.location = location
        self.is_spy = is_spy

    def __str__(self):
        return f"{self.name} - Spy: {self.is_spy}, Location: {self.location if not self.is_spy else 'Unknown'}"
