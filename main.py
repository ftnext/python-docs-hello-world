import json
import logging
from logging.handlers import RotatingFileHandler
from platform import python_version

from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
formatter = logging.Formatter(
    "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
handler.setFormatter(formatter)
app.logger.setLevel(logging.INFO) # app.run(debug=False)でinfo以下のログを出すために必要らしい
app.logger.addHandler(handler)

@app.route('/')
def hello_world():
    sentence = 'Hello, World! This is Python {}'
    return sentence.format(python_version())

@app.route('/response', methods=['POST'])
def print_data():
    parsed = json.loads(request.data)
    app.logger.info(json.dumps(parsed, indent=2))
    response = jsonify({'foo': 'bar'})
    response.status_code = 200
    return response


if __name__ == '__main__':
    app.run()
