"""
Created: 30.09
my_utils hold useful functions for the whole application
"""
from global_controller.global_controller import Global_Controller
from flask import make_response, jsonify

def set_global_controller(gc: Global_Controller):
    gc.update(Global_Controller.SHUTDOWN, False)

def create_response (body, status):
    response = make_response(jsonify(body), status)
    response.headers.add('Access-Control-Allow-Origin', 'http://127.0.0.1:5000')
    return response