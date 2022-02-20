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


elfStances = Stances(nature=10,industry=2,war=2,magic=7)
orcStances = Stances(nature=1,industry=6,war=10,magic=4)
humanStances = Stances(nature=5,industry=7,war=6,magic=5)
dwarfStances = Stances(nature=2,industry=10,war=7,magic=1)