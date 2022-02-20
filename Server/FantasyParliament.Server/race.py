from stances import Stances

class Race:
    def __init__(self, name, stances):
        self.name = name
        self.stances = stances

    def serialize(self):
        return {'name': self.name,
                'stances': self.stances.serialize()}


