#!/usr/local/bin/python3

#TODO modularise this file

# Web framework imports
from flask import Flask, render_template

# system imports
from datetime import datetime
import json

# CmdMessenger service
from services import py_cmd_messenger

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


if __name__ == '__main__':
    pyCmdMessenger = py_cmd_messenger.PyCmdMessenger(1, "Messenger-thread", APP)
    pyCmdMessenger.start()
    APP.run(debug=DEBUG)
