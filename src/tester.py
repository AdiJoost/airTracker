from asyncio.log import logger
from gpio_handler import GPIO_Handler
from log.logger import Logger

def main():
    gpio_handler = GPIO_Handler()
    temp = gpio_handler.get_temperature()
    humidity = gpio_handler.get_humidity()
    Logger.log_csv(({temp},{humidity}))


if __name__ == "__main__":
    main()