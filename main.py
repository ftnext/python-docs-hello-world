import json

from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)

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
