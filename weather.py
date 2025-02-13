from urllib.request import urlopen
import json
import gps
import time

def get_weather_url(lat, lon):
    return f"https://api.weather.gov/points/{lat},{lon}"

def fetch_json(url):
    with urlopen(url) as response:
        return json.loads(response.read())

def print_weather():
    myGPS = gps.GPS()
    # time.sleep(2)
    myGPS.update()
    
    while True:
        weatherURL = get_weather_url(myGPS.lat(), myGPS.lon())
        if weatherURL != get_weather_url("n/a", "n/a"):
            break

    print(weatherURL)
    weather_data = fetch_json(weatherURL)
    forecast_url = weather_data['properties']['forecast']
    print(forecast_url)
    asOfTime = time.strftime("Weather as of %H:%M:%S %Z on %m %b %Y   ",time.localtime(time.time()))
    print(asOfTime)
    
    forecast_data = fetch_json(forecast_url)
    periods = forecast_data['properties']['periods']
    
    for period in periods[:2]:  # Print details for the first two periods
        print(f"{period['name']}: {period['shortForecast']}")
        print(f"Temperature: {period['temperature']} {period['temperatureUnit']}")
        print(f"Wind: {period['windSpeed']} {period['windDirection']}")
        print(f"Details: {period['detailedForecast']}\n")

if __name__ == "__main__":
    print_weather()
