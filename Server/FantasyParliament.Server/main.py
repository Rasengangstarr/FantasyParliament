#!/usr/bin/env python
# encoding: utf-8
from gettext import find
from realm import CreateRealms
from politician import generatePoliticians
from party import createParties 

import json
from flask import Flask

app = Flask(__name__)

#create the state
realms = CreateRealms(10);
politicians = generatePoliticians(10);

parties = createParties(politicians, 5)

@app.route('/')
def index():
    return json.dumps({})

@app.route('/realms')
def getRealms():
    return json.dumps([r.serialize() for r in realms])

@app.route('/politicians')
def getPoliticians():
    return json.dumps([p.serialize() for p in politicians])

@app.route('/parties')
def getParties():
    return json.dumps([p.serialize() for p in parties])

app.run()

