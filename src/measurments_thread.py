from log.logger import Logger
from datetime import datetime
import time
import threading
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
        
    def stop(self):
        self.deamon_thread.join(20)

    def run (self):
        self.gc.update(Global_Controller.MEASURE_DEMON,
                        Global_Controller.IS_ONLINE,
                        True)
        try:
            is_stop = False
            intervall = self.gc.get_arg(Global_Controller.MEASURE_DEMON,
                                        Global_Controller.MEASURMENT_INTERVALL)
            update_intervall = self.gc.get_arg(Global_Controller.MEASURE_DEMON,
                                        Global_Controller.MEASURMENT_UPDATE)
            counter = 0
            while not is_stop:
                self.gc.update(Global_Controller.MEASURE_DEMON,
                                Global_Controller.IS_ONLINE,
                                True)
                controls = self.gc.get()
                intervall = controls[Global_Controller.MEASURE_DEMON]\
                                    [Global_Controller.MEASURMENT_INTERVALL]
                update_intervall = controls[Global_Controller.MEASURE_DEMON]\
                                    [Global_Controller.MEASURMENT_UPDATE]
                if (controls[Global_Controller.MEASURE_DEMON][Global_Controller.SHUTDOWN] == True):
                    is_stop = True
                
                

                
                counter += 1
                if (counter == update_intervall):
                    readout = self.GPIO_Handler.read_co2()
                    record_time = datetime.now()
                    data = (readout["temerature"],
                        self.GPIO_Handler.get_humidity(),
                        readout["pressure"],
                        readout["co2"],
                        record_time.hour,
                        record_time.minute,
                        record_time.second,)
                    Logger.log_csv(data, f"{record_time.year}-{record_time.month}-{record_time.day}")
                    self.call_nerves(data)
                    counter = 0
                time.sleep(intervall)
        
            Logger.log(__name__, f"Deamon is dead")
            self.gc.update(Global_Controller.MEASURE_DEMON,
                            Global_Controller.IS_ONLINE, False)

        except Exception as e:
            Logger.log(__name__, e.args, "error_log.txt")
        
    
    def call_nerves(self, data):
        self.gc.update_arg(Global_Controller.TEMPERATURE, data=data[0])
        self.gc.update_arg(Global_Controller.HUMIDITY, data=data[1])
        self.gc.update_arg(Global_Controller.PRESSURE, data=data[2])
        self.gc.update_arg(Global_Controller.CO2, data=data[3])

    
