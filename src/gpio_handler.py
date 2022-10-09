"""
GPIO_handler handles all interactions with the GPIO on PI.
Since it is not thread-Safe, make sure, that every method is 
only used in one script.
"""

#import adafruit_dht
#import board
#from src.gpio_calls import read_co2_sensor, gpio_setup
from random import randint
from log.logger import Logger


class GPIO_Handler():
    def __init__(self):
        #self.dht_sensor = adafruit_dht.DHT11(board.D21)
        

        self.setup()
        
        



    def setup(self):
#        gpio_setup()

        return 1

    def get_humidity(self):
        has_valid_result = False
        humidity = randint(30,60)
        while not has_valid_result:
            try:
                #humidity = self.dht_sensor.humidity
                has_valid_result = True
            except:
                continue
        return humidity

    def read_co2(self):
        data = {
        "co2" : 1500,
        "temerature" : 22.5,
        "pressure" : 911.2,
        "valid" : False
        }
#        data = read_co2_sensor()
        if data == -1:
            Logger.log(__name__, "timeout on reading Co2 sensor", "error_log.txt")
        return data
    