from log.logger import Logger
from datetime import datetime
import time
import threading
from queue import Queue
from global_controller.global_controller import Global_Controller

class Measurment_Thread():

    def __init__(self, GPIO_Handler):
        self.GPIO_Handler = GPIO_Handler
        self.gc = Global_Controller()


    def start(self):
        try:
            self.deamon_thread = threading.Thread(target=self.run,
                                                  args=())
            self.deamon_thread.start()
            Logger.log(__name__, "Measurment-Deamon is running")
        except Exception as e:
            Logger.log(__name__, str(e), "error_log.txt")

    def run (self):
            is_stop = False
            while not is_stop:
                if (self.gc.get_arg(Global_Controller.SHUTDOWN) == True):
                    is_stop = True
                try:
                        record_time = datetime.now()
                        data = (self.GPIO_Handler.get_temperature(),
                                self.GPIO_Handler.get_humidity(),
                                record_time.hour,
                                record_time.minute,
                                record_time.second,)
                        Logger.log_csv(data, f"{record_time.year}-{record_time.month}-{record_time.day}")
                        time.sleep(2)
                except Exception as e:
                    Logger.log(__name__, str(e), "error_log.txt")
            Logger.log(__name__, f"Deamon is dead")
    
    def stop(self):
        self.deamon_thread.join(20)