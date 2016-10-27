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
        "rocket_state": json.loads(APP.rocket_state.replace("'", "\""))
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

@APP.route('/start_command')
def start_command():
    response = APP.pyCmdMessenger.send_start_command()
    if response is not None:
        return response[0] + "," + (':'.join(response[1]))
    else:
        return "No response to start command"

@APP.route('/skip_command')
def skip_command():
    response = APP.pyCmdMessenger.send_skip_command()
    if response is not None:
        return response[0] + "," + (':'.join(response[1]))
    else:
        return "No response to skip command"

@APP.route('/begin_command')
def begin_command():
    response = APP.pyCmdMessenger.send_begin_command()
    if response is not None:
        return response[0] + "," + (':'.join(response[1]))
    else:
        return "No response to begin command"

if __name__ == '__main__':
    APP.rocket_state = "{}"
    APP.pyCmdMessenger = py_cmd_messenger.PyCmdMessenger(1, "Messenger-thread", APP)
    APP.pyCmdMessenger.start()
    APP.run(debug=DEBUG)
