"""
Only works on pi, functions are imported to gpio_handler to
reduce amount of # needed to be removed for pi setup
"""
from smbus import SMBus
import time
import RPi.GPIO as GPIO

def read_co2_sensor():
    #The way the co2 sensor is read out is
    #a transformet script from
    # https://pi3g.com/rpi-co2
    EE895ADDRESS = 0x5E
    I2CREGISTER = 0x00
    i2cbus = SMBus(1)
    return_data={
        "co2" : -1,
        "temerature" : -1,
        "pressure" : -1,
        "valid" : False
    }
    for _ in range(10):
        read_data = i2cbus.read_i2c_block_data(EE895ADDRESS, I2CREGISTER, 8)

        co2 = read_data[0].to_bytes(1, 'big') + read_data[1].to_bytes(1, 'big')
        return_data["co2"] = int.from_bytes(co2, "big")

        temperature = read_data[2].to_bytes(1, 'big') + read_data[3].to_bytes(1, 'big')

        return_data["temerature"] = int.from_bytes(temperature, "big") / 100
        resvd = read_data[4].to_bytes(1, 'big') + read_data[5].to_bytes(1, 'big')
        resvd = int.from_bytes(resvd, "big")

        pressure = read_data[6].to_bytes(1, 'big') + read_data[7].to_bytes(1, 'big')
        return_data["pressure"] = int.from_bytes(pressure, "big") / 10
        if (resvd == 32768):
            return_data["valid"] = True
            return return_data
        time.sleep(1)
    return -1

def set_led(pin: int, on: bool):
    GPIO.output(pin, on)

def gpio_setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(20, GPIO.OUT)
    GPIO.setup(21, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    
