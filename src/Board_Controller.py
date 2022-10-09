"""
This Class handles all interactions with GPIO's and is the only class, that is responsible for
writing to csv-data-files.
"""

import time
from datetime import datetime
from log.logger import Logger
from src.gpio_handler import GPIO_Handler
from src.measurments_thread import Measurment_Thread
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
            self.GPIO_Handler = GPIO_Handler()
            self.measurment_thread = Measurment_Thread(self.GPIO_Handler)
            

            
    def start_messurments(self, intervall):
        try:
            self.measurment_thread.start()
        except Exception as e:
            Logger.log(__name__, str(e), "error_log.txt")

    
    def stop_messurments(self):
        self.measurment_thread.stop()
        pass

    def is_messurment_online(self):
        gc = Global_Controller()
        is_online = gc.get_arg(Global_Controller.MEASURE_DEMON)
        if not is_online:
            return False
        gc.update(Global_Controller.MEASURE_DEMON, False)
        time.sleep(int(gc.get_arg(Global_Controller.MEASURMENT_INTERVALL)) + 1)
        return gc.get_arg(Global_Controller.MEASURE_DEMON)
        
