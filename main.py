import json
import logging
from logging.handlers import RotatingFileHandler
import os

from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)
log_file_path = os.environ['MY_FLASK_LOG']
handler = RotatingFileHandler(log_file_path, maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO) # INFOより上のレベルを表示するらしい
formatter = logging.Formatter(
    "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
handler.setFormatter(formatter)
app.logger.setLevel(logging.INFO) # app.run(debug=False)でinfo以下のログを出すために必要らしい
app.logger.addHandler(handler)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/response', methods=['POST'])
def print_data():
    parsed = request.get_json()
    app.logger.info(json.dumps(parsed, indent=2))
    response = jsonify({'foo': 'bar'})
    response.status_code = 200
    return response


if __name__ == '__main__':
    app.run()
