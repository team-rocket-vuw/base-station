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
    app.lat = app.lat + 0.0005
    app.long = app.long + 0.0005

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
                'lat': -41.2880647,
                'long': 174.7617035
            },
            'target': {
                'lat': app.lat,
                'long': app.long
            },
            'request_url': api_url
        },
        'markers': [
          {
            'position': {
                'lat': -41.2880647,
                'lng': 174.7617035
                },
            'label': 'C',
            'key': 'current',
          },
          {
            'position': {
                'lat': app.lat,
                'lng': app.long
                },
            'label': 'R',
            'key': 'target',
          }
        ],
    }

    return json.dumps(data)


if __name__ == '__main__':
    app.lat = -41.2880647
    app.long = 174.7617035
    app.run(debug=DEBUG)
