import time
import weather
import os

if __name__ == "__main__":
    timeHack = time.time()
    os.system('clear')
    prettyNow = time.strftime(" %H:%M:%S %Z   \n %a %m %b %Y   ",time.localtime(time.time()))
    print(prettyNow)
    print()
    weather.print_weather()
    print("\033[0;0H", end="")

    while True:
        time.sleep(1)
        if time.time() - timeHack > 180:
            os.system('clear')
            print("\033[0;0H", end="")
            prettyNow = time.strftime(" %H:%M:%S %Z   \n %a %m %b %Y   ",time.localtime(time.time()))
            print(prettyNow)
            print()
            timeHack = time.time()
            weather.print_weather()
            print("\033[0;0H", end="")
        else:
            print()
            prettyNow = time.strftime(" %H:%M:%S %Z   \n %a %m %b %Y   ",time.localtime(time.time()))
            print(prettyNow)
            print("\033[0;0H", end="")


