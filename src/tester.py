from asyncio.log import logger
from gpio_handler import GPIO_Handler
from log.logger import Logger
import time

def main():
    gpio_handler = GPIO_Handler()
    temp = gpio_handler.get_temperature()
    humidity = gpio_handler.get_humidity()
    Logger.log_csv(({temp},{humidity}))
    while True:
        humidity = gpio_handler.get_humidity()
        temperature = gpio_handler.get_temperature()
        print(f"Temperature: {temperature}, Humidity: {humidity}")
        time.sleep(2)


if __name__ == "__main__":
    main()