"""
Date: 29.09.2022, 14:13
Author: Adrian Joost
This Class handles a controler.json file.
"""
import os
from filelock import FileLock
from log.logger import Logger
import json
import time

class Global_Controller():
    SHUTDOWN = "shutdown"
    BLINKING_SHOW = "blinking_show"
    #Resolution of Measurments in seconds
    MEASURMENT_INTERVALL = "measurment_intervall"
    #How many measurments pass before updating controls.json
    MEASURMENT_UPDATE = "measurment_update"
    HUMIDITY = "humidity"
    TEMPERATURE = "temperature"
    CO2 = "co2"
    PRESSURE = "pressure"
    MAIL_LIST = "mail_list"
    MEASURE_DEMON = "measure_deamon"
    MAIL_DEAMON = "mail_deamon"
    LED_DEAMON = "led_deamon"
    IS_ONLINE = "is_online"
    thread_names = (
        MEASURE_DEMON,
        MAIL_DEAMON,
        LED_DEAMON
    )

    def __init__(self):
        self.lock_path = self.get_file_path("controls.json.lock")
        self.file_path = self.get_file_path("controls.json")
        self.file_lock = FileLock(self.lock_path, 3600)
        
    def get_file_path(self, file):
        my_path = os.getcwd().split("airTracker", 1)[0]
        my_path = os.path.join(my_path, "airTracker", "global_controller", file)
        return my_path
    
    def get(self):
        with self.file_lock:
            with open(self.file_path, "r") as file:
                data = file.read()
        return json.loads(data)

    def get_arg(self, key):
        with self.file_lock:
            with open(self.file_path, "r") as file:
                data = json.loads(file.read())
        if key in data.keys():
            return data[key]
        else:
            Logger.log(__name__, f"Asked global Controller for non existing key({key})")
    
    def get_arg(self, thread_key, key):
        with self.file_lock:
            with open(self.file_path, "r") as file:
                data = json.loads(file.read())
        if thread_key in data.keys():
            if key in data[thread_key].keys():
                return data[thread_key][key]
        else:
            Logger.log(__name__, f"Asked global Controller for non existing key([{thread_key}][{key}])")


    def append(self, data):
        with self.file_lock:
            with open(self.file_path, "a") as file:
                success = file.write(json.dumps(data))
        return success
    
    def update_arg(self, key: str, data=""):
        with self.file_lock:
            with open(self.file_path, "r") as file:
                old_data = json.loads(file.read())
            old_data[key] = data
            self.overwrite(old_data)
        return {key: old_data[key]}
    
    def update(self, thread_key: str, key: str, data=""):
        with self.file_lock:
            with open(self.file_path, "r") as file:
                old_data = json.loads(file.read())
            old_data[thread_key][key] = data
            self.overwrite(old_data)
        return {key: old_data[thread_key][key]}

    
    def overwrite(self, data=""):
        with self.file_lock:
            with open(self.file_path, "w") as file:
                success = file.write(json.dumps(data))
        return success
    
    def is_online(self, meassure_name):
        self.update(meassure_name, self.IS_ONLINE, False)
        time.sleep(int(self.get_arg(meassure_name, Global_Controller.MEASURMENT_INTERVALL)) + 2)
        return self.get_arg(meassure_name, self.IS_ONLINE)