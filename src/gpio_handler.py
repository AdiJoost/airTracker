#import adafruit_dht

class GPIO_Handler():
    def __init__(self):
        #self.dhtService = adafruit_dht.DHT11(board.D4)
        self.gas_sensor_analog = 14
        self.gas_sensor_digital = 15
        

    def setup(self):
        pass

    def get_humidity(self):
        #return self.dhtService.temperature
        return 70

    def get_temperature(self):
        #return self.dhtService.humidity
        return 25