#import Adafruit_DHT

class GPIO_Handler():
    def __init__(self):
        #self.DHT_SENSOR = Adafruit_DHT.DHT11
        self.gas_sensor_analog = 14
        self.gas_sensor_digital = 15
        self.DHT_PIN = 4
        
        

    def setup(self):
        pass

    def get_humidity(self):
        #humidity, _ = Adafruit_DHT.read(self.DHT_SENSOR, self.DHT_PIN)
        #return humidity
        return 70

    def get_temperature(self):
        #_, temperature = Adafruit_DHT.read(self.DHT_SENSOR, self.DHT_PIN)
        #return temperature
        return 25