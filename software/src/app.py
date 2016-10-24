#!/usr/local/bin/python3

#TODO modularise this file

# Web framework imports
from flask import Flask, render_template

# helpers
from services import map_url_generator

# system imports
from datetime import datetime
import threading
import json
import time

# CmdMessenger import
import PyCmdMessenger

#TODO remove this. Here for testing only
from random import randint

SERIAL_PORT = "/dev/cu.usbmodem1411"
BAUD_RATE = 9600

ARDUINO_INTERFACE = PyCmdMessenger.ArduinoBoard(SERIAL_PORT, baud_rate = BAUD_RATE)

MESSENGER_COMMANDS= [["rocket_location",""],
                    ["rocket_location_is","s"],
                    ["send_rocket_command","i"],
                    ["rocket_command_response","s"],
                    ["error","s"]]

MESSENGER = PyCmdMessenger.CmdMessenger(ARDUINO_INTERFACE, MESSENGER_COMMANDS)

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


class MessengerThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        while True:
            MESSENGER.send("rocket_location")
            response = MESSENGER.receive()
            location = response[1][0]
            formatted_string = location.replace("/.", ".").split(",")
            formatted_location = list(map(float, formatted_string))
            APP.lat = formatted_location[0]
            APP.lng = formatted_location[1]


if __name__ == '__main__':
    messengerThread = MessengerThread(1, "Messenger-thread")
    messengerThread.start()
    APP.run(debug=DEBUG)
