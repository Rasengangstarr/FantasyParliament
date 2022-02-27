#!/usr/bin/env python
# encoding: utf-8
from gettext import find
from realm import CreateRealms
from politician import generatePoliticians
from party import createParties
from event import Event
from event import EventType
import threading

import json
import time
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


#create the state
realms = CreateRealms(52);
politicians = generatePoliticians(100);

parties = createParties(politicians, 5)

events = []

nextEventId = 0

logging = 1

def declareElection(id, dateStr):
    value =  Event(id, "A General Election will occur in 10 days!", dateStr, EventType.ELECTION_CALLED, [])
    print ("Declaring election")
    return value

def runElection(id, dateStr):
    value =  Event(id, "A General Election is occuring!", dateStr, EventType.ELECTION_HAPPENING, [])
    print ("Running election")
    return value

def mainLoop(events, politicians, realms):
    eId = 0
    hour = 0
    day = 0
    year = 0
    while True:
        eventsForTick = []
        #handle time
        hour+=1
        if hour == 24:
            hour = 0
            day += 1
            print("day " + str(day))
        if day == 300:
            day = 0
            year += 1
        time.sleep(1)
        dateStr = "year: " + str(year) + " day: " + str(day) + " hour: " + str(hour)
        #handle globalEvents
        if hour == 1 and day == 0:
            eventsForTick.append(declareElection(eId, dateStr))
            eId += 1
        elif hour == 0 and day == 1:
            eventsForTick.append(runElection(eId, dateStr))
            eId += 1
        eventsToRespondTo = []
        for e in eventsForTick:
            if (len(e.targetMembers) == 0):
                for p in politicians:
                    if e.type == EventType.ELECTION_CALLED:
                        p.handleElectionCalled(politicians, realms)
                for r in realms:
                    if e.type == EventType.ELECTION_HAPPENING:
                        eventsToRespondTo.append(r.handleElection(eId, dateStr))
                        eId += 1

        events += eventsForTick + eventsToRespondTo
        #print ([str(e.id)+" - "+e.name for e in events])

x = threading.Thread(target=mainLoop, args=(events,politicians,realms,)) 
x.start()


@app.route('/')
@cross_origin()
def index():
    return json.dumps({})

@app.route('/realms')
@cross_origin()
def getRealms():
    return json.dumps([r.serialize() for r in realms])

@app.route('/politicians')
@cross_origin()
def getPoliticians():
    return json.dumps([p.serialize(parties) for p in politicians])

@app.route('/parties')
@cross_origin()
def getParties():
    return json.dumps([p.serialize() for p in parties])

@app.route('/parties/detailed')
@cross_origin()
def getPartiesDetailed():
    return json.dumps([p.serialize_detailed(politicians) for p in parties])

@app.route('/events')
@cross_origin()
def getEvents():
    return json.dumps([e.serialize() for e in events])

app.run()

