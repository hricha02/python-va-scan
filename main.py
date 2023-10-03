
from tokenize import String

from flask import app, Flask
from flask import Flask, jsonify, request, make_response
import os
from datetime import datetime, time, date
import requests
from flask_oidc import OpenIDConnect
import logging
import psycopg2
from functools import wraps
from flask import abort
import json

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
ASSETS_DIR = os.path.dirname(os.path.abspath(__file__))


app = Flask(__name__)


APPLICATION_ROOT = '/'
app.config['APPLICATION_ROOT'] = APPLICATION_ROOT
app.config.from_object(__name__)

APPLICATION_ROOT = '/cengine'
app.config['APPLICATION_ROOT'] = APPLICATION_ROOT
app.config.from_object(__name__)


@app.route(APPLICATION_ROOT+'/executeScript', methods = ['POST'])
def scriptExecutor_grpc():
            logging.info("request start Update")
            return make_response(jsonify("success"), 200)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9093)

