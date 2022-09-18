"""
This Class handles all interactions with GPIO's and is the only class, that is responsible for
writing to csv-data-files.
"""

import threading
import time
from datetime import datetime
from log.logger import Logger
from gpio_handler import GPIO_Handler

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
            self.stop_event = threading.Event()
            
            
    def start_daemon_thread(self):
        """starts deamon_thread to execute orders in self.queue. Deamon will
        check after given intervall for new orders and executes them"""
        try:
            Logger.log(__name__, "setup Deamon", "daemon_log.txt")
            self.deamon_thread = threading.Thread(target=self.run_queue,
                                                  args=(self.stop_event,))
            self.deamon_thread.start()
            Logger.log(__name__, "Deamon is running", "daemon_log.txt")
        except Exception as e:
            Logger.log(__name__, str(e), "error_log.txt", "daemon_log.txt")
    
    def stop_daemon_thread(self):
        Logger.log(__name__, "Stopping daemon-thread", "daemon_log.txt")
        self.stop_event.set()
        Logger.log(__name__, "Event set", "daemon_log.txt")
        self.deamon_thread.join()
        Logger.log(__name__, "Daemon is dead", "daemon_log.txt")

            
    def run_queue (self, event):
        Logger.log(__name__, "Queue started", "daemon_log.txt")
        while not event.is_set():
            try:
                    record_time = datetime.now()
                    data = (self.GPIO_Handler.get_temperature(),
                            self.GPIO_Handler.get_humidity(),
                            record_time.hour,
                            record_time.minute,
                            record_time.second)
                    Logger.log_csv(data, f"{record_time.year}-{record_time.month}-{record_time.day}")
                    time.sleep(2)
            except Exception as e:
                Logger.log(__name__, str(e), "error_log.txt")
        

