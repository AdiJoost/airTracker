#import adafruit_dht
#import board
from random import randint

class GPIO_Handler():
    def __init__(self):
        #self.dht_sensor = adafruit_dht.DHT11(board.D4)
        self.gas_sensor_analog = 14
        self.gas_sensor_digital = 15
        
        

    def setup(self):
        pass

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

    def get_temperature(self):
        has_valid_result = False
        temperature = randint(17,35)
        while not has_valid_result:
            try:
                #temperature = self.dht_sensor.temperature
                has_valid_result = True
            except:
                continue
        return temperature