#!/usr/local/bin/python3

#TODO modularise this file

# Web framework imports
from flask import Flask, render_template, request

# system imports
from datetime import datetime
import json
import requests

# CmdMessenger service
from services import py_cmd_messenger

# OpenRocket service
from services import open_rocket_simulations

#TODO remove this. Here for testing only
from random import randint

APP = Flask(__name__)
DEBUG = True

@APP.route('/')
def index():
    return render_template('index.html')

@APP.route('/data')
def data():
    data = {
        'status': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'gyro': {
            'x': randint(0, 100),
            'y': randint(0, 100),
            'z': randint(0, 100)
        },
        'location': {
            'target': {
                'lat': APP.lat,
                'lng': APP.lng
            }
        },
        'markers': [
          {
            'position': {
                'lat': APP.lat,
                'lng': APP.lng
                },
            'label': 'R',
            'key': 'target'
          }
        ],
    }

    return json.dumps(data)

@APP.route('/simulations')
def simulations():
    service = open_rocket_simulations.OpenRocketSimulations()
    data = service.run_simulations()

    return data

@APP.route('/weather', methods=['POST'])
def weather():
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    APPID = request.args.get('APPID')
    response = requests.get(url="http://api.openweathermap.org/data/2.5/weather?lat=" + lat + "&lon=" + lng + "&APPID=" + APPID)
    return json.dumps(response.json())


if __name__ == '__main__':
    APP.lat = 0
    APP.lng = 0
    pyCmdMessenger = py_cmd_messenger.PyCmdMessenger(1, "Messenger-thread", APP)
    pyCmdMessenger.start()
    APP.run(debug=DEBUG)
