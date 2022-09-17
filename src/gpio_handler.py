#import adafruit_dht

class GPIO_Handler():
    def __init__(self):
        #self.DHT_SENSOR = adafruit_dht.DHT11
        self.gas_sensor_analog = 14
        self.gas_sensor_digital = 15
        self.DHT_PIN = 4
        
        

    def setup(self):
        pass

    def get_humidity(self):
        #humidity, _ = adafruit_dht.read(self.DHT_SENSOR, self.DHT_PIN)
        #return humidity
        return 70

    def get_temperature(self):
        #_, temperature = adafruit_dht.read(self.DHT_SENSOR, self.DHT_PIN)
        #return temperature
        return 25