import requests
import random
import json
from politician import Politician

class Realm:
    def __init__(self, name, population, racePops):
        self.name = name
        self.population = population
        self.racePops = racePops

    def serialize(self):
        return {'name': self.name,
                'population': self.population,
                'racePops': self.racePops.serialize()
                }


class RacePops:
    def __init__(self, elfPop=1, orcPop=1, humanPop=1, dwarfPop=1):
        totalPop = elfPop + orcPop + humanPop + dwarfPop
        assert totalPop > 0
        self.elfPop = elfPop/totalPop
        self.orcPop = orcPop/totalPop
        self.humanPop = humanPop/totalPop
        self.dwarfPop = dwarfPop/totalPop

    def serialize(self):
        return {'elfPop': self.elfPop,
                'orcPop': self.orcPop,
                'humanPop': self.humanPop,
                'dwarfPop': self.dwarfPop}


def CreateRealms(count):
    numBatches = count / 10
    currentCount = 0
    currentBatch = 0
    realms = []
    while (currentBatch < numBatches):
        names = json.loads(requests.get(
            "https://donjon.bin.sh/name/rpc-name.fcgi?type=Town&n=10&as_json=1").content)

        nameCount = 0
        while (currentCount < 10 and currentCount < count):
            realms += [Realm(n, random.randint(100, 1000),
                             RacePops(elfPop=getRandPop(), orcPop=getRandPop(), humanPop=getRandPop(), dwarfPop=getRandPop()))
                       for n in names]
            currentCount += 1
        currentBatch += 1

    return realms


def getRandPop():
    return random.randint(1, 10)
