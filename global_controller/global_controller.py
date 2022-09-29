"""
Date: 29.09.2022, 14:13
Author: Adrian Joost
This Class handles a controler.json file.
"""
import json
from src.external_source.fileLocker.filelock.filelock import FileLock

class Global_Controller():
    def __init__(self):
        with FileLock("controles.json") as file:
            my_json = file.read()
            print(my_json)