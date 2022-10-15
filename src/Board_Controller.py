"""
This Class handles all interactions with GPIO's and is the only class, that is responsible for
writing to csv-data-files.
"""

import time
from datetime import datetime
from log.logger import Logger
from src.gpio_handler import GPIO_Handler
from src.measurments_thread import Measurment_Thread
from src.led_thread import LED_Thread
from global_controller.global_controller import Global_Controller



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
            self.gc = Global_Controller()
            self.GPIO_Handler = GPIO_Handler()
            self.measurment_thread = Measurment_Thread(self.GPIO_Handler)
            self.led_thread = LED_Thread(self.GPIO_Handler)

            

            
    def start_messurments(self):
        try:
            self.measurment_thread.start()
        except Exception as e:
            Logger.log(__name__, str(e), "error_log.txt")
    
    def start_led(self):
        try:
            self.led_thread.start()
        except Exception as e:
            Logger.log(__name__, str(e), "error_log.txt")

    
    def stop_messurments(self):
        self.measurment_thread.stop()
        pass

    def start_thread(self, thread_name: str):
        #this is a bad use, but restruction of thread-handling
        #is more timeconsuming than using an if-elif
        
        
        if (thread_name == Global_Controller.MEASURE_DEMON):
            Logger.log(__name__, "start a Measure deamon")
            self.gc.update(Global_Controller.MEASURE_DEMON,
                            Global_Controller.SHUTDOWN, False)
            self.start_messurments()

        if (thread_name == Global_Controller.LED_DEAMON):
            Logger.log(__name__, "start an LED deamon")
            self.gc.update(Global_Controller.LED_DEAMON,
                            Global_Controller.SHUTDOWN, False)
            self.start_led()