from itertools import count
from stances import Stances
import requests
import random
import json

class Politician:
    def __init__(self, name, loyalty, race, principled, stances):
        self.name = name
        self.loyalty = loyalty
        self.race = race
        self.principled = principled
        self.stances = stances

    def serialize(self):
        return {'name': self.name,
                'loyalty': self.loyalty,
                'race': self.race,
                'principled': self.principled,
                'stances': self.stances.serialize()}


def generatePoliticians(countOfEach):
    elfNames = requests.get(
            "https://story-shack-cdn-v2.glitch.me/generators/elf-name-generator?count="+str(countOfEach)).json()["data"]
    orcNames = requests.get(
            "https://story-shack-cdn-v2.glitch.me/generators/orc-name-generator?count="+str(countOfEach)).json()["data"]
    dwarfNames = requests.get(
            "https://story-shack-cdn-v2.glitch.me/generators/dwarf-name-generator?count="+str(countOfEach)).json()["data"]
    humanNames = requests.get(
            "https://story-shack-cdn-v2.glitch.me/generators/human-name-generator?count="+str(countOfEach)).json()["data"]

    politicians = []
    for e in elfNames:
        politicians.append(Politician(e["male"]+" "+e["female"],random.randint(0,10), "elf", random.randint(0,10),
        Stances(nature=10,industry=2,war=2,magic=7)))
    for o in orcNames:
        politicians.append(Politician(o["male"]+" "+o["female"],random.randint(0,10), "orc", random.randint(0,10),
        Stances(nature=1,industry=6,war=10,magic=4)))
    for h in humanNames:
        politicians.append(Politician(h["female"]+" "+h["male"],random.randint(0,10), "human", random.randint(0,10),
        Stances(nature=5,industry=7,war=6,magic=5)))
    for d in dwarfNames:
        politicians.append(Politician(d["male"]+" "+d["female"],random.randint(0,10), "dwarf", random.randint(0,10),
        Stances(nature=2,industry=10,war=7,magic=1)))
    return politicians
