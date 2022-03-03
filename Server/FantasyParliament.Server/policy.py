from enum import IntEnum
from stances import Stances

class Policies(IntEnum):
    NONE = 0 
    TEAR_DOWN_FOREST_FOR_IND = 1

class Policy():
    def __init__(self, id, name, stances):
        self.id = id
        self.name = name
        self.stances = stances

def generatePolicies():
    policies = []
    policies.append(Policy(Policies.TEAR_DOWN_FOREST_FOR_IND, "Tear down the forests to build factories", Stances(nature=0, industry=10, war=5, magic=5)))
    return policies