import time
import weather
if __name__ == "__main__":
    timeHack = time.time()
    while True:
        if time.time() - timeHack > 180:
            os.system('clear')
            timeHack = time.time()
            weather.print_weather()



