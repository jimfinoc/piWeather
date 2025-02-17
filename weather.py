from urllib.request import urlopen 
from dotenv import load_dotenv
import json
import time
import os
import redis

def get_weather_url(lat, lon):
    return f"https://api.weather.gov/points/{lat},{lon}"

def fetch_json(url):
    with urlopen(url) as response:
        return json.loads(response.read())

def print_weather():
    while True:
        lat = 'n/a'
        lon = 'n/a'
        try:
            import gps
            print('-try gps.GPS()')
            myGPS = gps.GPS()
            lat = myGPS.lat()
            lon = myGPS.lon()
            # myGPS.update()
            print (f"Lat: {lat}, Lon: {lon}")
            print ("gps data loaded from function")
        except:
            print("=error getting database from the gps source")
        if lat == 'n/a' and lon == 'n/a':
            try:
                print('-try loading file .My_location.json')
                filename = ".My_location.json"
                with open(filename, "r") as file:
                    My_location = json.load(file)
                lat = My_location['Lat']
                lon = My_location['Lon']
                print ("gps data loaded from file")
            except:
                print ("=error getting data from file")
        if lat == 'n/a' and lon == 'n/a':
            try:
                print('-try redis database')
                load_dotenv(".env")
                print ("redis_database_name")
                print (" ",os.getenv("redis_database_name"))
                print ("redis_database_port")
                print (" ",os.getenv("redis_database_port"))
                print ("redis_database_password")
                print (" ",os.getenv("redis_database_password"))
                r = redis.Redis(db=0,host=os.getenv("redis_database_name"),port=os.getenv("redis_database_port"),password=os.getenv("redis_database_password"))
                My_location_json_string = r.get('My_location')
                My_location = json.loads(My_location_json_string)
                print("My_location")
                print(My_location)
                lat = My_location['Lat']
                lon = My_location['Lon']
            except:
                print ("=error getting data from database")
        if lat != 'n/a' and lon != 'n/a':
            print ("Lat:",lat)
            print ("Lon:",lon)
            break

    weatherURL = get_weather_url(lat,lon)
    # print()
    # print("weatherURL")
    # print(weatherURL)
    # print()
    weather_data = fetch_json(weatherURL)
    # print()
    # print("weather_data")
    # print(weather_data)
    # print()

    forecast_url = weather_data['properties']['forecast']
    print()
    print("forecast_url")
    print(forecast_url)
    asOfTime = time.strftime("Weather as of %H:%M:%S %Z on %m %b %Y   ",time.localtime(time.time()))
    print(asOfTime)
    print()
    
    forecast_data = fetch_json(forecast_url)
    periods = forecast_data['properties']['periods']
    
    for period in periods[:2]:  # Print details for the first two periods
        print(f"{period['name']}: {period['shortForecast']}")
        print(f"Temperature: {period['temperature']} {period['temperatureUnit']}")
        print(f"Wind: {period['windSpeed']} {period['windDirection']}")
        print(f"Details: {period['detailedForecast']}\n")

if __name__ == "__main__":
    print_weather()
