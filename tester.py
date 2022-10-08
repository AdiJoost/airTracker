#from Board_Controller import Board_Controller
from log.logger import Logger
import time
from global_controller.global_controller import Global_Controller
from src.gpio_handler import GPIO_Handler
import datetime
import threading
import json

def main():
    
    gh = GPIO_Handler()
    while True:
        read_dht(gh)
        time.sleep(2)

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

    
    """
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