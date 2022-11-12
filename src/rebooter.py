from log.logger import Logger
from datetime import datetime
import time
import threading
from src.my_utils import reboot
from global_controller.global_controller import Global_Controller

class Rebooter():

    def __init__(self):
        self.gc = Global_Controller()


    def start(self):
        try:
            self.deamon_thread = threading.Thread(target=self.run,
                                                  args=())
            self.deamon_thread.start()
            Logger.log(__name__, "Rebooter is running")
        except Exception as e:
            Logger.log(__name__, str(e), "error_log.txt")
        
    def stop(self):
        self.deamon_thread.join(20)

    def run (self):
        self.gc.update(Global_Controller.REBOOTER,
                        Global_Controller.IS_ONLINE,
                        True)
        try:
            is_stop = False
            intervall = self.gc.get_arg(Global_Controller.REBOOTER,
                                        Global_Controller.MEASURMENT_INTERVALL)
            update_intervall = self.gc.get_arg(Global_Controller.REBOOTER,
                                        Global_Controller.MEASURMENT_UPDATE)
            counter = 0
            while not is_stop:
                self.gc.update(Global_Controller.REBOOTER,
                                Global_Controller.IS_ONLINE,
                                True)
                controls = self.gc.get()
                intervall = controls[Global_Controller.REBOOTER]\
                                    [Global_Controller.MEASURMENT_INTERVALL]
                update_intervall = controls[Global_Controller.REBOOTER]\
                                    [Global_Controller.MEASURMENT_UPDATE]
                if (controls[Global_Controller.REBOOTER][Global_Controller.SHUTDOWN] == True):
                    is_stop = True
                
                

                
                counter += 1
                if (counter == update_intervall):
                    now = datetime.now()
                    Logger.log(__name__, "Check Reboot")
                    if now.hour in controls[Global_Controller.REBOOTER]\
                        [Global_Controller.REBOOT_TIME]:
                        Logger.log(__name__, "Rebooting...")
                        reboot()
                time.sleep(intervall)
        
            Logger.log(__name__, f"Rebooter is dead")
            self.gc.update(Global_Controller.MEASURE_DEMON,
                            Global_Controller.IS_ONLINE, False)

        except Exception as e:
            Logger.log(__name__, e.args, "error_log.txt")
        
    
    def call_nerves(self, data):
        self.gc.update_arg(Global_Controller.TEMPERATURE, data=data[0])
        self.gc.update_arg(Global_Controller.HUMIDITY, data=data[1])
        self.gc.update_arg(Global_Controller.PRESSURE, data=data[2])
        self.gc.update_arg(Global_Controller.CO2, data=data[3])

    
