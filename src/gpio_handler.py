#import adafruit_dht
#import board

class GPIO_Handler():
    def __init__(self):
        #self.dht_sensor = adafruit_dht.DHT11(board.D4)
        self.gas_sensor_analog = 14
        self.gas_sensor_digital = 15
        
        

    def setup(self):
        pass

    def get_humidity(self):
        #return self.dht_sensor.humidity
        return 70

    def get_temperature(self):
        #return adafruit_dht.temperature
        return 25