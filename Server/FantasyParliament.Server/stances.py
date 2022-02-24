from race import Races
from background import Backgrounds

class Stances:
    def __init__(self, nature=1, industry=1, war=1, magic=1):
        
        totalStance = nature+industry+war+magic
        
        assert totalStance > 0
        self.nature = nature/totalStance
        self.industry = industry/totalStance
        self.war = war/totalStance
        self.magic = magic/totalStance

    def serialize(self):
        return {'nature': self.nature,
                'industry': self.industry,
                'war': self.war,
                'magic': self.magic}

racialStances = {
    Races.ELF: Stances(nature=10, industry=2, war=2, magic=7),
    Races.DWARF: Stances(nature=2, industry=10, war=7, magic=1),
    Races.ORC: Stances(nature=1, industry=6, war=10, magic=4),
    Races.HUMAN: Stances(nature=5, industry=7, war=6, magic=5)
}

backgroundStances = {
    Backgrounds.CRAFTSMAN: Stances(industry=9, war=5, magic=3, nature=3),
    Backgrounds.MAGE: Stances(industry=2, war=2, nature=5, magic=9),
    Backgrounds.RANGER: Stances(industry=1, nature=9, war=5, magic=6),
    Backgrounds.WARRIOR: Stances(war=9, nature=5, magic=4, industry=6)
}
