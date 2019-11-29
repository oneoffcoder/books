from flask import Flask, jsonify, request, Response, abort
from flask_cors import CORS
import json
import time
import os

app = Flask(__name__)
app.config.from_object('config')
CORS(app, resources={r'/*': {'origin': '*'}})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return json.dumps({'message': app.config['AUTHOR']})


@app.route('/v1/test', methods=['GET'])
def hello():
    return json.dumps({
        'author': app.config['AUTHOR'],
        'app_name': app.config['APP_NAME'],
        'timestamp': current_milli_time()
    })


@app.route('/v1/db', methods=['GET'])
def db_params():
    return json.dumps({
        'DB_USER': get_env_value('DB_USER', app.config['DB_USER']),
        'DB_PW': get_env_value('DB_PW', app.config['DB_PW']),
        'DB_INSTANCE': get_env_value('DB_INSTANCE', app.config['DB_INSTANCE']),
        'DB_HOST': get_env_value('DB_HOST', app.config['DB_HOST']),
        'DB_PORT': get_env_value('DB_PORT', app.config['DB_PORT']),
        'timestamp': current_milli_time()
    })


def current_milli_time():
    return int(round(time.time() * 1000))


def get_env_value(key, def_val):
    return os.getenv(key, def_val)


if __name__ == '__main__':
    port = get_env_value('FLASK_PORT', 5000)

    app.run(debug=True, host='0.0.0.0', port=port)