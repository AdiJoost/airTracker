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

class Board_Controller():
    __instance = None
    thread_controls = {"shutdown": False,
                        "lightshow": False}
    
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
            self.kill_daemon = False
            self.shared_data = Queue()
            thread_controls = {"shutdown": False,
                                "lightshow": False}
            self.shared_data.put(thread_controls)

            
    def start_daemon_thread(self):
        """starts deamon_thread to execute orders in self.queue. Deamon will
        check after given intervall for new orders and executes them"""
        try:
            Logger.log(__name__, "setup Deamon", "daemon_log.txt")
            self.deamon_thread = threading.Thread(target=self.run_queue,
                                                  args=(self.shared_data, self.thread_controls))
            self.deamon_thread.start()
            Logger.log(__name__, "Deamon is running", "daemon_log.txt")
        except Exception as e:
            Logger.log(__name__, str(e), "error_log.txt", "daemon_log.txt")
    
    def stop_daemon_thread(self):
        controls = self.shared_data.get()
        controls["shutdown"] = True
        self.thread_controls["shutdown"] = True
        self.shared_data.put(controls)
        #self.deamon_thread.join()
        Logger.log(__name__, "Daemon is dead - Well, it does not listen to me so it is still alive, give it some space", "daemon_log.txt")

    def start_lightshow(self):
        """starts a thread with a lightshow"""
        try:
            Logger.log(__name__, "setup Deamon", "daemon_log.txt")
            self.lightshow = threading.Thread(target=self.light_up,
                                                  args=())
            self.lightshow.start()
            Logger.log(__name__, "lightshow is running")
        except Exception as e:
            Logger.log(__name__, str(e), "error_log.txt")

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
        

