from tomlkit import datetime
from log.logger import Logger
import time
import threading
from global_controller.global_controller import Global_Controller
import MailBot.MailBot as mb
import os

class Mail_Thread():

    def __init__(self, GPIO_Handler):
        self.GPIO_Handler = GPIO_Handler
        self.gc = Global_Controller()


    def start(self):
        try:
            self.deamon_thread = threading.Thread(target=self.run,
                                                  args=())
            self.deamon_thread.start()
            Logger.log(__name__, "Mail-Deamon is running")
        except Exception as e:
            Logger.log(__name__, str(e), "error_log.txt")
        
    def stop(self):
        self.deamon_thread.join(20)

    def run (self):
        self.gc.update(Global_Controller.MAIL_DEAMON,
                        Global_Controller.IS_ONLINE,
                        True)
        try:
            is_stop = False
            should_send = True
            intervall = self.gc.get_arg(Global_Controller.MAIL_DEAMON,
                                        Global_Controller.MEASURMENT_INTERVALL)

            while not is_stop:
                self.gc.update(Global_Controller.MAIL_DEAMON,
                                Global_Controller.IS_ONLINE,
                                True)
                controls = self.gc.get()
                if (controls[Global_Controller.MAIL_DEAMON][Global_Controller.SHUTDOWN] == True):
                    is_stop = True
                
                now = time.localtime()
                if(now.tm_hour == 19 and should_send):
                    try:
                        self.send_mail()
                        should_send = False
                    except Exception as e:
                        Logger.log(__name__, str(e), "error_log.txt")
                if(now.tm_hour == 20):
                    should_send = True

                time.sleep(intervall)
                
        
            Logger.log(__name__, f"Mail-Deamon is dead")
            self.GPIO_Handler.tell_gpio(21, False)
            self.gc.update(Global_Controller.MAIL_DEAMON,
                            Global_Controller.IS_ONLINE, False)

        except Exception as e:
            Logger.log(__name__, e.args, "error_log.txt")
    
    def send_mail(self):
        mail_list = self.gc.get_arg(Global_Controller.MAIL_DEAMON,
                                    Global_Controller.MAIL_LIST)
        path = self.get_path()
        for user in mail_list:
            text = f"Hello {user}:\n\n Here is your Data from yesterday\n\nkind Regards\nairTracker"
            mb.sendMail(text, "Your Report", mail_list[user], path)
            Logger.log(__name__, f"Mail sent to: {mail_list[user]}")

    def get_path(self):
        my_path = os.getcwd().split("airTracker", 1)[0]
        my_path = os.path.join(my_path, "airTracker", "log", f"2022-10-7.csv")
        return my_path