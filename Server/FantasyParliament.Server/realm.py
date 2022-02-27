from cmath import log10
from sqlite3 import Row
import requests
import random
import json
from job import Jobs
from event import Event
from politician import Politician
from event import EventType
from perlin_noise import PerlinNoise

class Realm:
    def __init__(self, id, name, row, column, realmType, population, racePops):
        self.id = id
        self.name = name
        self.row = row 
        self.column = column
        self.population = population
        self.racePops = racePops
        self.realmType = realmType
        self.member = -1 
        self.candidates = []

    def serialize(self):
        return {'name': self.name,
                'row':self.row,
                'column':self.column,
                'type': self.realmType,
                'population': self.population,
                'racePops': self.racePops.serialize(),
                'candidates': [c.serialize() for c in self.candidates],
                'member': self.member.serialize()
                }
    def handleElection(self, id, dateStr):
        self.member = self.candidates[random.randint(0, len(self.candidates)-1)]
        if self.member.job == Jobs.CANDIDATE:
            self.member.job = Jobs.MEMBER
        return Event(id, self.member.name + " has been elected to represent " + self.name, dateStr, EventType.CANDIDATE_ELECTED_TO_REALM, [])


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
    noise = PerlinNoise(octaves=1)
    realms = []
    row = 0
    col = 0
    names = json.loads(requests.get(
        "https://donjon.bin.sh/name/rpc-name.fcgi?type=Ward&n="+str(count)+"&as_json=1").content)

    for i in range(0,count):
        if (row % 2 != 0 and col == 6) or col == 7:
            row = row + 1
            col = 0

        if row % 2 != 0:
            colForView = col+0.5
        else:
            colForView = col
        realmNoiseValue = noise([colForView+2/6,row+2/6])


        if realmNoiseValue < -0.15:
            realmType = 0
            realms.append(Realm(i, names[i], row, col, realmType, random.randint(100, 1000),
                    RacePops(elfPop=getRandPop(), orcPop=getRandBoostedPop(), humanPop=getRandPop(), dwarfPop=getRandPop())))
        elif realmNoiseValue < 0:
            realmType = 1
            realms.append(Realm(i, names[i], row, col, realmType, random.randint(100, 1000),
                    RacePops(elfPop=getRandPop(), orcPop=getRandPop(), humanPop=getRandBoostedPop(), dwarfPop=getRandPop())))
        elif realmNoiseValue < 0.15:
            realmType = 2
            realms.append(Realm(i, names[i], row, col, realmType, random.randint(100, 1000),
                    RacePops(elfPop=getRandBoostedPop(), orcPop=getRandPop(), humanPop=getRandPop(), dwarfPop=getRandPop())))
        else:
            realmType = 3 
            realms.append(Realm(i, names[i], row, col, realmType, random.randint(100, 1000),
                    RacePops(elfPop=getRandPop(), orcPop=getRandPop(), humanPop=getRandPop(), dwarfPop=getRandBoostedPop())))
        
        col = col + 1
    return realms

def getRandPop():
    return random.randint(1, 10)
def getRandBoostedPop():
    return random.randint(10, 20)
