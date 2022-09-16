from gpio_handler import GPIO_Handler

def main():
    gpio_handler = GPIO_Handler()
    print(f"Temp: {gpio_handler.get_temperature()} | Humidity: {gpio_handler.get_humidity()}")


if __name__ == "__main__":
    main()