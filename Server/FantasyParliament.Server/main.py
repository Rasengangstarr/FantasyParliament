#!/usr/bin/env python
# encoding: utf-8
import json
from race import Race 
from race import Stances

from realm import Realm
from realm import CreateRealms

from politician import Politician
from politician import generatePoliticians 

from stances import elfStances
from stances import orcStances
from stances import humanStances
from stances import dwarfStances


from flask import Flask

app = Flask(__name__)

elves = Race("elves", elfStances)
orcs = Race("orcs", orcStances)
humans = Race("humans", humanStances)
dwarves = Race("dwarves", dwarfStances)

#create the state
races = [elves, orcs, humans, dwarves]
realms = CreateRealms(95);
politicians = generatePoliticians(95);

@app.route('/')
def index():
    return json.dumps({'name': 'alice',
                       'email': 'alice@outlook.com'})

@app.route('/races')
def getRaces():
    return json.dumps([r.serialize() for r in races])

@app.route('/realms')
def getRealms():
    return json.dumps([r.serialize() for r in realms])

@app.route('/politicians')
def getPoliticians():
    return json.dumps([p.serialize() for p in politicians])

app.run()

