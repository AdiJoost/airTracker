"""
Author: Adrian Joost
Created: September, 2022
Note:

Remove all # to enable proper functionallity on actual AirTracker.
With # in, the Software is in Simulation-Mode.
GPIO_handler handles all interactions with the GPIO on PI.
Since it is not thread-Safe, make sure, that every method is 
only used in one script.
"""


#import board
#from src.gpio_calls import read_co2_sensor, gpio_setup, set_led
from random import randint
from log.logger import Logger


class GPIO_Handler():
    RED = "red"
    BLUE = "blue"
    GREEN = "green"
    YELLOW = "yellow"
    PURPLE = "purple"
    TURN_OFF ="turn_off"
    def __init__(self):

        self.redPin = 20
        self.bluePin = 21
        self.greenPin = 26

        self.setup()
        
        



    def setup(self):
#        gpio_setup()

        return 1
    
    def tell_gpio(self, color):
        if color == self.RED:
#            set_led(self.redPin, True)
#            set_led(self.bluePin, False)
#            set_led(self.greenPin, False)
            pass
        elif color == self.BLUE:
#            set_led(self.redPin, False)
#            set_led(self.bluePin, True)
#            set_led(self.greenPin, False)
            pass
        elif color == self.GREEN:
#            set_led(self.redPin, False)
#            set_led(self.bluePin, False)
#            set_led(self.greenPin, True)
            pass
        elif color == self.YELLOW:
#            set_led(self.redPin, True)
#            set_led(self.bluePin, False)
#            set_led(self.greenPin, True)
            pass
        elif color == self.PURPLE:
#            set_led(self.redPin, True)
#            set_led(self.bluePin, True)
#            set_led(self.greenPin, False)
            pass
        elif color == self.TURN_OFF:
#            set_led(self.redPin, False)
#            set_led(self.bluePin, False)
#            set_led(self.greenPin, False)
            pass

        return 1

    def get_humidity(self):
        has_valid_result = False
        humidity = randint(30,60)
        while not has_valid_result:
            try:

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
    