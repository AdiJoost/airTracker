#from Board_Controller import Board_Controller
from log.logger import Logger
import time
from global_controller.global_controller import Global_Controller
from src.gpio_handler import GPIO_Handler
import datetime
import threading
import json
from MailBot.MailBot import *
import os

def main():
    path = get_path()
    sendMail(text= "hello",subject="Test", reciver="adi.joost@gmail.com", path=path)

def get_path():
    try:
        my_path = os.getcwd().split("airTracker", 1)[0]
        my_path = os.path.join(my_path, "airTracker", "log", f"main_log.txt")
        return my_path
    except Exception as e:
        Logger.log(__name__, e.args, "error_log.txt")
        my_path = os.getcwd().split("airTracker", 1)[0]
        my_path = os.path.join(my_path, "airTracker", "log", f"notFound.txt")
    
"""
    gh = GPIO_Handler()
    while True:
        
        gh.blink()
        

def read_dht(gh):
    print(gh.get_humidity())



def ask_controller(number, timeo=2):
    print(f"Controler {number} started")
    gc = Global_Controller()
    data = gc.get()
    time.sleep(timeo)
    gc.update("Hello", True)
    print(data)
    print(type(data))

    
    
    gpio_handler = GPIO_Handler()
    while True:
        humidity = gpio_handler.get_humidity()
        temperature = gpio_handler.get_temperature()
        stamper = datetime.datetime.now()
        Logger.log_csv((temperature, humidity, stamper.hour, stamper.minute, stamper.second, stamper.timestamp()),
         f"temp_humidity{stamper.year}-{stamper.month}-{stamper.day}")
        print(f"Temperature: {temperature}, Humidity: {humidity}")
        time.sleep(2)
    board_controller = Board_Controller()
    board_controller.start_daemon_thread()
    time.sleep(5)
    Logger.log(__name__, "I'm running")
    time.sleep(5)
    board_controller.stop_daemon_thread()
    Logger.log(__name__, "Going to stop")
    
    for _ in range(10):
        with FileLock("requirements.txt"):
            print("File open")
        print("file closed")"""

if __name__ == "__main__":
    main()