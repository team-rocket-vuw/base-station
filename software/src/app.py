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
        "rocket_state": APP.rocket_state,
        'location': {
            'target': {
                'lat': 0,
                'lng': 0
            }
        },
        'markers': [
          {
            'position': {
                'lat': 0,
                'lng': 0
                },
            'label': 'R',
            'key': 'target'
          }
        ],
    }

    print(json.dumps(data))

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

@APP.route('/start_command')
def start_command():
    response = APP.pyCmdMessenger.send_start_command()
    response_string = response[0] + "," + (':'.join(response[1]))
    return response_string

@APP.route('/skip_command')
def skip_command():
    response = APP.pyCmdMessenger.send_skip_command()
    response_string = response[0] + "," + (':'.join(response[1]))
    return response_string

@APP.route('/begin_command')
def begin_command():
    response = APP.pyCmdMessenger.send_begin_command()
    response_string = response[0] + "," + (':'.join(response[1]))
    return response_string

if __name__ == '__main__':
    APP.rocket_state = {}
    APP.lat = 0
    APP.lng = 0
    APP.pyCmdMessenger = py_cmd_messenger.PyCmdMessenger(1, "Messenger-thread", APP)
    APP.pyCmdMessenger.start()
    APP.run(debug=DEBUG)
