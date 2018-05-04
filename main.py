import json
import logging
from logging.handlers import RotatingFileHandler

from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
log = logging.getLogger('werkzeug')
log.setLevel(logging.INFO)
log.addHandler(handler)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/response', methods=['POST'])
def print_data():
    parsed = json.loads(request.data)
    # TODO: parsedをログに出力
    response = jsonify({'foo': 'bar'})
    response.status_code = 200
    return response


if __name__ == '__main__':
    app.run()
