"""
Date: 29.09.2022, 14:13
Author: Adrian Joost
This Class handles a controler.json file.
"""
import os
from filelock import FileLock
from log.logger import Logger
import json

class Global_Controller():
    SHUTDOWN = "shutdown"
    BLINKING_SHOW = "blinking_show"

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

    def append(self, data):
        with self.file_lock:
            with open(self.file_path, "a") as file:
                success = file.write(json.dumps(data))
        return success
    
    def update(self, key: str, data=""):
        with self.file_lock:
            with open(self.file_path, "r") as file:
                old_data = json.loads(file.read())
            old_data[key] = data
            self.overwrite(old_data)
        return {key: old_data[key]}

    
    def overwrite(self, data=""):
        with self.file_lock:
            with open(self.file_path, "w") as file:
                success = file.write(json.dumps(data))
        return success