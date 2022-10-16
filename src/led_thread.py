from log.logger import Logger
import time
import threading
from global_controller.global_controller import Global_Controller

class LED_Thread():

    def __init__(self, GPIO_Handler):
        self.GPIO_Handler = GPIO_Handler
        self.gc = Global_Controller()


    def start(self):
        try:
            self.deamon_thread = threading.Thread(target=self.run,
                                                  args=())
            self.deamon_thread.start()
            Logger.log(__name__, "LED-Deamon is running")
        except Exception as e:
            Logger.log(__name__, str(e), "error_log.txt")
        
    def stop(self):
        self.deamon_thread.join(20)

    def run (self):
        self.gc.update(Global_Controller.LED_DEAMON,
                        Global_Controller.IS_ONLINE,
                        True)
        try:
            is_stop = False
            intervall = self.gc.get_arg(Global_Controller.LED_DEAMON,
                                        Global_Controller.MEASURMENT_INTERVALL)

            while not is_stop:
                self.gc.update(Global_Controller.LED_DEAMON,
                                Global_Controller.IS_ONLINE,
                                True)
                controls = self.gc.get()
                if (controls[Global_Controller.LED_DEAMON][Global_Controller.SHUTDOWN] == True):
                    is_stop = True
                co2 = controls[Global_Controller.CO2]
                t1 = controls[Global_Controller.LED_DEAMON][Global_Controller.T1]
                t2 = controls[Global_Controller.LED_DEAMON][Global_Controller.T2]
                t3 = controls[Global_Controller.LED_DEAMON][Global_Controller.T3]
                t4 = controls[Global_Controller.LED_DEAMON][Global_Controller.T4]
                
                if (co2 < t1):
                    self.GPIO_Handler.tell_gpio(21, True)
                    time.sleep(intervall * 1)
                elif (co2 < t2):
                    self.GPIO_Handler.tell_gpio(21, True)
                    time.sleep(intervall * 0.95)
                    self.GPIO_Handler.tell_gpio(21, False)
                    time.sleep(intervall * 0.05)
                elif (co2 < t3):
                    for _ in range(2):
                        self.GPIO_Handler.tell_gpio(21, True)
                        time.sleep(intervall * 0.33)
                        self.GPIO_Handler.tell_gpio(21, False)
                        time.sleep(intervall * 0.33)
                elif (co2 < t4):
                    for _ in range(5):
                        self.GPIO_Handler.tell_gpio(21, True)
                        time.sleep(intervall * 0.1)
                        self.GPIO_Handler.tell_gpio(21, False)
                        time.sleep(intervall * 0.1)
                else:
                    for _ in range(10):
                        self.GPIO_Handler.tell_gpio(21, True)
                        time.sleep(intervall * 0.05)
                        self.GPIO_Handler.tell_gpio(21, False)
                        time.sleep(intervall * 0.05)
                

                
                
        
            Logger.log(__name__, f"LED-Deamon is dead")
            self.GPIO_Handler.tell_gpio(21, False)
            self.gc.update(Global_Controller.LED_DEAMON,
                            Global_Controller.IS_ONLINE, False)

        except Exception as e:
            Logger.log(__name__, e.args, "error_log.txt")