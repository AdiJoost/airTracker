"""
Created: 30.09
my_utils hold useful functions for the whole application
"""
from global_controller.global_controller import Global_Controller
from flask import make_response, jsonify
import os
from time import sleep
from log.logger import Logger

def set_global_controller(gc: Global_Controller):
    for name in gc.thread_names:
        gc.update(name, gc.SHUTDOWN, False)

def create_response (body, status):
    response = make_response(jsonify(body), status)
    response.headers.add('Access-Control-Allow-Origin', 'http://127.0.0.1:5000')
    return response

def deamon_hunt():
    """Gracefully shuts all deamons down"""
    gc = Global_Controller()
    for thread_name in Global_Controller.thread_names:
        gc.update(thread_name, gc.SHUTDOWN, True)

def reboot():
    deamon_hunt()
    sleep(5)
    Logger.log(__name__, "Reboot")
    os.system("sudo shutdown -r")