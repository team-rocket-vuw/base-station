#!/usr/local/bin/python3

from flask import Flask, render_template
import json

from services import map_url_generator

from datetime import datetime
from random import randint

app = Flask(__name__)

DEBUG = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    app.lat = app.lat + 0.0001
    app.long = app.long + 0.0001

    downloader = map_url_generator.MapURLGenerator((app.lat, app.long), (-41.288712, 174.761792))
    api_url = downloader.generate_url()

    data = {
        'status': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'gyro': {
            'x': randint(0, 100),
            'y': randint(0, 100),
            'z': randint(0, 100)
        },
        'location': {
            'current': {
                'lat': randint(0, 100),
                'long': randint(0, 100)
            },
            'target': {
                'lat': randint(0, 100),
                'long': randint(0, 100)
            },
            'request_url': api_url
        }
    }

    return json.dumps(data)


if __name__ == '__main__':
    app.lat = -41.2880647
    app.long = 174.7617035
    app.run(debug=DEBUG)