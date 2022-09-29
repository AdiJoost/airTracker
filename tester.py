#from Board_Controller import Board_Controller
from log.logger import Logger
import time
from global_controller.global_controller import Global_Controller
import datetime
import threading
import json

def main():
    print("Main started")
    Logger.log(__name__, "Tester started")
    thread_1 = threading.Thread(target=ask_controller, args=(1,))
    thread_2 = threading.Thread(target=ask_controller, args=(2,))
    thread_1.start()
    thread_2.start()


def ask_controller(number):
    print(f"Controler {number} started")
    gc = Global_Controller()
    data = gc.get()
    gc.update("shutdown", True)
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