import time
import weather
import os

if __name__ == "__main__":
    timeHack = time.time()
    os.system('clear')
    timeHack = time.time()
    prettyNow = time.strftime(" %H:%M:%S %Z   \n %a %m %b %Y   ",time.localtime(time.time()))
    print(prettyNow)
    print("\033[1;1H", end="")
    print()
    weather.print_weather()

    while True:
        time.sleep(1)
        if time.time() - timeHack > 180:
            os.system('clear')
            prettyNow = time.strftime(" %H:%M:%S %Z   \n %a %m %b %Y   ",time.localtime(time.time()))
            print(prettyNow)
            print()
            timeHack = time.time()
            weather.print_weather()
            print("\033[1;1H", end="")
        else:
            prettyNow = time.strftime(" %H:%M:%S %Z   \n %a %m %b %Y   ",time.localtime(time.time()))
            print(prettyNow)
            print("\033[1;1H", end="")


