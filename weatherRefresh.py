import time
import weather
import os

def prettyTime():
    return time.strftime(" %H:%M:%S %Z on %a %m %b %Y   ",time.localtime(time.time()))


if __name__ == "__main__":
    refreshTime = 300
    timeHack = time.time()
    os.system('clear')
    prettyNow = prettyTime()
    print(prettyNow)
    print()
    weather.print_weather()
    print("\033[0;0H", end="")

    while True:
        time.sleep(1)
        if time.time() - timeHack > refreshTime:
            os.system('clear')
            print("\033[0;0H", end="")
            prettyNow = prettyTime()
            print(prettyNow)
            print()
            timeHack = time.time()
            weather.print_weather()
            print("\033[0;0H", end="")
        else:
            prettyNow = prettyTime()
            print(prettyNow)
            print("\033[0;0H", end="")


