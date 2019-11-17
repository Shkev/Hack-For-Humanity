#!/usr/bin/env python

import flask

from flask import Flask
from flask import request
from flask import render_template

import sys
sys.path.append('./utils')

# Create the application.
APP = Flask(__name__)

@APP.route('/events', methods=['GET'])
def events():
    return render_template('events.html')

@APP.route('/resources', methods=['GET'])
def resources():
    return render_template('resources.html')


@APP.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index.html')


if __name__ == '__main__':
    APP.debug = True
    APP.run()
