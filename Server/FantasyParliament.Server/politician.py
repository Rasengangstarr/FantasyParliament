from stances import racialStances
from stances import backgroundStances
from stances import Stances
from race import Races 
import requests
import random

class Politician:
    def __init__(self, id, name, race, background, loyalty, steadfastness, charisma, intelligence):
        self.id = id 
        self.name = name
        self.loyalty = loyalty
        self.race = race
        self.steadfastness = steadfastness 
        self.charisma = charisma
        self.intelligence = intelligence
        self.background = background
        self.stances = Stances(1,1,1,1) 
        self.generateStances(self.background, self.race, 2) 
        self.knownEvents = []
        self.relationships = []

    def serialize(self):
        return {'name': self.name,
                'loyalty': self.loyalty,
                'steadfastness': self.steadfastness,
                'charisma': self.charisma,
                'intelligence': self.intelligence,
                'race': self.race,
                'background': self.background,
                'stances': self.stances.serialize()}

    def generateStances(self, background, race, modifier):
        self.stances.industry = backgroundStances[background].industry + racialStances[race].industry + random.randint(0,modifier)/10 
        self.stances.war = backgroundStances[background].war + racialStances[race].war + random.randint(0,modifier)/10 
        self.stances.nature = backgroundStances[background].nature + racialStances[race].nature + random.randint(0,modifier)/10
        self.stances.magic = backgroundStances[background].magic + racialStances[race].magic + random.randint(0,modifier)/10 
    

def generatePoliticians(countOfEach):
    elfNames = requests.get(
            "https://story-shack-cdn-v2.glitch.me/generators/elf-name-generator?count="+str(countOfEach)).json()["data"]
    orcNames = requests.get(
            "https://story-shack-cdn-v2.glitch.me/generators/orc-name-generator?count="+str(countOfEach)).json()["data"]
    dwarfNames = requests.get(
            "https://story-shack-cdn-v2.glitch.me/generators/dwarf-name-generator?count="+str(countOfEach)).json()["data"]
    humanNames = requests.get(
            "https://story-shack-cdn-v2.glitch.me/generators/human-name-generator?count="+str(countOfEach)).json()["data"]
    
    thisId = 0
    
    politicians = []
    for e in elfNames:
        background = random.randint(1,4)
        politicians.append(Politician(thisId, e["male"]+" "+e["female"],
             Races.ELF,
             background,
             random.randint(0,10),
             random.randint(0,10),
             random.randint(0,10),
             random.randint(0,10)
        ))
        thisId += 1
    for o in orcNames:
        background = random.randint(1,4)
        politicians.append(Politician(thisId, o["male"]+" "+o["female"],
             Races.ORC,
             background,
             random.randint(0,10),
             random.randint(0,10),
             random.randint(0,10),
             random.randint(0,10)
        ))
        thisId += 1    
        
    for h in humanNames:
        background = random.randint(1,4)
        politicians.append(Politician(thisId, h["female"]+" "+h["male"],
             Races.HUMAN,
             background,
             random.randint(0,10),
             random.randint(0,10),
             random.randint(0,10),
             random.randint(0,10)
        ))
        thisId += 1    
        
    for d in dwarfNames:
        background = random.randint(1,4)
        politicians.append(Politician(thisId, d["female"]+" "+d["male"],
             Races.DWARF,
             background,
             random.randint(0,10),
             random.randint(0,10),
             random.randint(0,10),
             random.randint(0,10)
        ))
        thisId += 1    

    return politicians
