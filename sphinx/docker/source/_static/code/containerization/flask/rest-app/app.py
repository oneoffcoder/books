from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import time

app = Flask(__name__)
app.config.from_object('config')
CORS(app, resources={r'/*': {'origin': '*'}})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return json.dumps({'message': app.config['AUTHOR']})


@app.route('/v1/test', methods=['GET'])
def hello():
    current_milli_time = lambda: int(round(time.time() * 1000))
    return json.dumps({
        'author': app.config['AUTHOR'],
        'app_name': app.config['APP_NAME'],
        'timestamp': current_milli_time()
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')