"""
This Class handles all interactions with GPIO's and is the only class, that is responsible for
writing to csv-data-files.
"""

import threading
from queue import Queue
import time
from datetime import datetime
from log.logger import Logger
from src.gpio_handler import GPIO_Handler
from src.measurments_thread import Measurment_Thread



class Board_Controller():
    __instance = None
    
    
    @staticmethod
    def get_instance():
        """returns the instance of the Board_Controller"""
        if Board_Controller.__instance == None:
            Board_Controller()
        return Board_Controller.__instance
    
    def __init__(self):
        """virtually privat constructor. App will call it once"""
        if Board_Controller.__instance is not None:
            raise Exception("This constructer can olny be called by the"\
                            " the class itself")
        else:
            Board_Controller.__instance = self
            self.GPIO_Handler = GPIO_Handler()
            self.thread_controls = {"shutdown": False,
                                    "lightshow": False,
                                    "counter": 1}
            self.measurment_thread = Measurment_Thread(self.GPIO_Handler, self.thread_controls)

            
    def start_messurments(self, intervall):
        try:
            self.measurment_thread.start()
        except Exception as e:
            Logger.log(__name__, str(e), "error_log.txt")
        """
        try:
            Logger.log(__name__, "setup meassurments thread", "meassurments_log.txt")
            self.deamon_thread = threading.Thread(target=self.measurment_thread.run,
                                                  args=(self.thread_controls,))
            self.deamon_thread.start()
            Logger.log(__name__, "Deamon is running", "meassurments_log.txt")
        except Exception as e:
            Logger.log(__name__, str(e), "error_log.txt")"""
    
    def stop_messurments(self):
        self.measurment_thread.stop()
        pass

   
    def run_queue (self, queue, thread_controls):
        Logger.log(__name__, "Queue started", "daemon_log.txt")
        is_shutdown = False
        try:
            controls = queue.get()
            is_shutdown = controls["shutdown"]
            queue.put(controls)
            Logger.log(__name__, f"Que has: {controls}", "daemon_log.txt")
        except Exception as e:
            Logger.log(__name__, str(e), "error_log.txt")

        while not is_shutdown:
            controls = queue.get()
            is_shutdown = controls["shutdown"]
            queue.put(controls)
            try:
                    thread_controls["counter"] += 1
                    record_time = datetime.now()
                    data = (self.GPIO_Handler.get_temperature(),
                            self.GPIO_Handler.get_humidity(),
                            record_time.hour,
                            record_time.minute,
                            record_time.second,
                            is_shutdown,
                            thread_controls)
                    Logger.log_csv(data, f"{record_time.year}-{record_time.month}-{record_time.day}")
                    time.sleep(2)
            except Exception as e:
                Logger.log(__name__, str(e), "error_log.txt")
        

