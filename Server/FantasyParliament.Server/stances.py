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
    Races.ELF: Stances(nature=10, industry=5, war=2, magic=7),
    Races.DWARF: Stances(nature=5, industry=10, war=7, magic=2),
    Races.ORC: Stances(nature=2, industry=7, war=10, magic=5),
    Races.HUMAN: Stances(nature=7, industry=2, war=5, magic=10)
}

backgroundStances = {
    Backgrounds.CRAFTSMAN: Stances(industry=10, war=2, magic=2, nature=2),
    Backgrounds.MAGE: Stances(industry=2, war=2, nature=2, magic=10),
    Backgrounds.RANGER: Stances(industry=2, nature=10, war=2, magic=2),
    Backgrounds.WARRIOR: Stances(war=10, nature=2, magic=2, industry=2)
}
