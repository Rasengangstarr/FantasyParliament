#!/usr/bin/env python
# encoding: utf-8
from gettext import find
from realm import CreateRealms
from politician import generatePoliticians
from party import createParties 

import json
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


#create the state
realms = CreateRealms(52);
politicians = generatePoliticians(100);

parties = createParties(politicians, 5)

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
    return json.dumps([p.serialize() for p in politicians])

@app.route('/parties')
@cross_origin()
def getParties():
    return json.dumps([p.serialize() for p in parties])

@app.route('/parties/detailed')
@cross_origin()
def getPartiesDetailed():
    return json.dumps([p.serialize_detailed(politicians) for p in parties])

app.run()

