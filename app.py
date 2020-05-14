# -*- encoding: utf-8 -*-

import os
import yaml
import flask

config_dict = {}
try:
    with open('.env.yaml', 'r') as config_stream:
        config_dict = yaml.safe_load(config_stream)
except Exception as e:
    print(e)

for config_name in config_dict:
    os.environ[config_name] = config_dict[config_name]

from main import handle

app = flask.Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    return handle(flask.request)
