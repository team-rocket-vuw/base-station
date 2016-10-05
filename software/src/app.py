from flask import Flask, render_template
import json

from random import randint

app = Flask(__name__)

DEBUG = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    data = {
        'foo': randint(0, 9)
    }
    return json.dumps(data)


if __name__ == '__main__':
    app.run(debug=DEBUG)