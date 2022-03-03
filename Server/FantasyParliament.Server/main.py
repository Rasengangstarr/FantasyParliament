#!/usr/bin/env python
# encoding: utf-8
from gettext import find
import re
from realm import CreateRealms
from politician import generatePoliticians
from party import createParties
from policy import Policies
from policy import Policy
from policy import generatePolicies
from event import Event
from event import EventType
from flask import request
from stances import diffStances

from random import randint
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

policies = generatePolicies()

events = []

nextEventId = 0

logging = 1

def declareElection(id, dateStr):
    value =  Event(id, "A General Election will occur in 10 days!", dateStr, EventType.ELECTION_CALLED, [])
    print ("Declaring election")
    return value

def runElection(id, dateStr):
    value =  Event(id, "A General Election is occuring!", dateStr, EventType.ELECTION_STARTED, [])
    print ("Running election")
    return value

def mainLoop(events, politicians, realms, policies):
    eId = 0
    hour = 0
    day = 0
    year = 0
    electionInProgress = False
    while True:
        eventsForTick = []
        eventsToRespondTo = []
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
        elif hour == 0 and day == 10:
            eventsForTick.append(runElection(eId, dateStr))
            electionRIndex = 0
            electionInProgress = True
            eId += 1
        elif hour == 2 and day == 0:
            #DEBATE
            policyToDebate = policies[randint(0,len(policies))-1]
            memberToRaiseMotion = politicians[0]
            eventsToRespondTo.append(Event(eId, memberToRaiseMotion.name + " moves to "+ policyToDebate.name, dateStr, EventType.DEBATE_STARTED, [])) 
            eId += 1

        for e in eventsForTick:

            if (len(e.targetMembers) == 0):
                for p in politicians:
                    if e.type == EventType.ELECTION_CALLED:
                        p.handleElectionCalled(politicians, realms)

        if electionInProgress:
            eventsToRespondTo.append(realms[electionRIndex].handleElection(eId, dateStr))
            eId += 1
            electionRIndex += 1
            if electionRIndex >= len(realms):
                electionInProgress = False

        for e in eventsToRespondTo:
            if e.type == EventType.DEBATE_STARTED:
                for m in politicians:
                    if diffStances(m.stances, policyToDebate.stances) > 1.4:
                        eventsForTick.append(Event(eId, m.name + "says THERE'S COLLUSION!", dateStr, EventType.DEBATE_RESPONSE, []))
                    else:
                        eventsForTick.append(Event(eId, m.name + "says POGGERS!", dateStr, EventType.DEBATE_RESPONSE, []))
                    eId += 1


        events += eventsToRespondTo + eventsForTick 
        #print ([str(e.id)+" - "+e.name for e in events])

x = threading.Thread(target=mainLoop, args=(events,politicians,realms,policies,)) 
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
    fromId = int(request.args.get("from"))
    return json.dumps([e.serialize() for e in events if e.id > fromId])

@app.route('/events/max')
@cross_origin()
def getEventsMax():
    return str(max([e.id for e in events])) 

app.run()