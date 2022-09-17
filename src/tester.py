from asyncio.log import logger
from gpio_handler import GPIO_Handler
from log.logger import Logger
import time
import datetime

def main():
    gpio_handler = GPIO_Handler()
    while True:
        humidity = gpio_handler.get_humidity()
        temperature = gpio_handler.get_temperature()
        stamper = datetime.datetime.now()
        Logger.log_csv((temperature, humidity, stamper.hour, stamper.minute, stamper.second, stamper.timestamp()),
         f"temp_humidity{stamper.year}-{stamper.month}-{stamper.day}")
        print(f"Temperature: {temperature}, Humidity: {humidity}")
        time.sleep(2)


if __name__ == "__main__":
    main()