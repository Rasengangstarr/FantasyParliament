from enum import IntEnum

class Event:
    def __init__(self, id, name, date, type, targetMembers):
        self.id = id
        self.name = name
        self.date = date 
        self.type = type
        self.targetMembers = targetMembers 
    
    def serialize(self):
        return {'id': self.id,
                'date': self.date,
                'name': self.name}

class EventType(IntEnum):
    ELECTION_CALLED = 1,
    ELECTION_HAPPENING = 2,
    ELECTION_FINISHED = 3,
    CANDIDATE_ELECTED_TO_REALM = 4
