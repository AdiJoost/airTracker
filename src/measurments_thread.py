from log.logger import Logger
from datetime import datetime
import time
import threading
from queue import Queue

class Measurment_Thread():

    def __init__(self, GPIO_Handler, thread_controls):
        self.GPIO_Handler = GPIO_Handler
        self.is_shutdown = False
        self.queue = Queue()
        self.thread_controls = thread_controls

    def start(self):
        try:
            Logger.log(__name__, "setup meassurments thread", "meassurments_log.txt")
            self.deamon_thread = threading.Thread(target=self.run,
                                                  args=(self.thread_controls, self.queue))
            self.deamon_thread.start()
            Logger.log(__name__, "Deamon is running", "meassurments_log.txt")
        except Exception as e:
            Logger.log(__name__, str(e), "error_log.txt")

    def run (self, thread_controls, queue):
            Logger.log(__name__, "run() called", "daemon_log.txt")
            is_stop = False
            while not is_stop:
                try:
                    controls = queue.get(block=False)
                    Logger.log(__name__, f"Got a queue :) {controls}", "error_log.txt")
                    if controls["shutdown"]:
                        Logger.log(__name__, f"is_stop is set {controls}", "error_log.txt")
                        is_stop = True
                        continue
                except:
                    Logger.log(__name__, "got no queue", "noqueue.txt")
                try:
                        thread_controls["counter"] += 1
                        record_time = datetime.now()
                        data = (self.GPIO_Handler.get_temperature(),
                                self.GPIO_Handler.get_humidity(),
                                record_time.hour,
                                record_time.minute,
                                record_time.second,
                                self.is_shutdown,
                                thread_controls)
                        Logger.log_csv(data, f"{record_time.year}-{record_time.month}-{record_time.day}")
                        time.sleep(2)
                except Exception as e:
                    Logger.log(__name__, str(e), "error_log.txt")
            Logger.log(__name__, f"While-loop exited", "error_log.txt")
    
    def stop(self):
        Logger.log(__name__, "Put something in queue")
        self.queue.put({
            "shutdown": True
        })
        self.deamon_thread.join()