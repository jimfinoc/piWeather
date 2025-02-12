import time
import weather
import os

if __name__ == "__main__":
    timeHack = time.time()
    os.system('clear')
    timeHack = time.time()
    prettyHack = time.strftime("%m/%d/%Y, %H:%M %Z",time.localtime(timeHack()))
    print(prettyHack)
    weather.print_weather()

    while True:
        if time.time() - timeHack > 180:
            os.system('clear')
            timeHack = time.time()
            prettyHack = time.strftime("%m/%d/%Y, %H:%M %Z",time.localtime(timeHack()))
            print(prettyHack)
            weather.print_weather()



