import tkinter as tk
import datetime
import math
import json
from urllib.request import urlopen 



window = tk.Tk()
my_geometry = 400
afterTime = 5 * 60 * 1000 # time is in milliseconds
x_geometry = my_geometry
y_geometry = my_geometry
pad = 10
padx = pad
pady = pad
window.geometry(f"{x_geometry}x{y_geometry}")
window.title("Weather Update")

def get_weather_url(lat, lon):
    return f"https://api.weather.gov/points/{lat},{lon}"

def fetch_json(url):
    print("url")
    print(url)
    with urlopen(url) as response:
        print("response")
        print(response)
        return json.loads(response.read())

def return_location():
    lat = 'n/a'
    lon = 'n/a'
    try:
        import redis
        from dotenv import load_dotenv
        import os
        # print('-try redis database')
        load_dotenv(".env")
        # print ("redis_database_name")
        # print (" ",os.getenv("redis_database_name"))
        # print ("redis_database_port")
        # print (" ",os.getenv("redis_database_port"))
        # print ("redis_database_password")
        # print (" ",os.getenv("redis_database_password"))
        r = redis.Redis(db=0,host=os.getenv("redis_database_name"),port=os.getenv("redis_database_port"),password=os.getenv("redis_database_password"))
        My_location_json_string = r.get('My_location')
        My_location = json.loads(My_location_json_string)
        print("My_location")
        print(My_location)
        lat = My_location['Lat']
        lon = My_location['Lon']
        print("lat")
        print(lat)
        print("lon")
        print(lon)
    except:
        pass
    return (lat,lon)

def return_weather():
    lat,lon = return_location()
    weatherURL = get_weather_url(lat,lon)

    filename = ".My_weather.json"
    weather_data = fetch_json(weatherURL)
    try:
        with open(filename, "w") as file:
            json.dump(weather_data, file, indent=4)
        pass
        # print(f"weatherURL saved to disk at {filename}")
    except:
        print(f"error writing to file {filename}")


    # print("weather_data")
    # print(weather_data)
    city = weather_data['properties']['relativeLocation']['properties']['city']
    state = weather_data['properties']['relativeLocation']['properties']['state']
    
    forecast_url = weather_data['properties']['forecast']
    forecast_data = fetch_json(forecast_url)
    # print("forecast_data")
    # print(forecast_data)
    periods = forecast_data['properties']['periods']    
    # print()
    for period in periods[:1]:  # Print details for the first two periods
        print(f"{period['name']}: {period['shortForecast']}")
        print(f"Temperature: {period['temperature']} {period['temperatureUnit']}")
        print(f"Wind: {period['windSpeed']} {period['windDirection']}")
        print(f"Details: {period['detailedForecast']}\n")
    return (city,state,periods[0],periods[1],periods[2])

# data = return_weather()
label = {}
label['location'] = tk.Label(window, font=("Arial", 30), text="")
label['period_1'] = tk.Label(window, font=("Arial", 20), text="")
label['period_2'] = tk.Label(window, font=("Arial", 10), text="")
label['period_3'] = tk.Label(window, font=("Arial", 10), text="")

def update_labels():
    data = return_weather()
    label['location'].config(text=f"{data[0]}, {data[1]}")
    label['period_1'].config(text=f"{data[2]['name']}\n\n{data[2]['detailedForecast']}", wraplength=my_geometry-10)

    label['period_2'].config(text=f"{data[3]['name']}\n{data[3]['shortForecast']}", wraplength=my_geometry/2-5)
    label['period_3'].config(text=f"{data[4]['name']}\n{data[4]['shortForecast']}", wraplength=my_geometry/2-5)
    window.after(afterTime, update_labels) #time to wait in milliseconds

update_labels()

# for key in label:
    # label[key].pack()
label['location'].grid(row=0,column=0,columnspan=2,sticky="nsew")
label['period_1'].grid(row=1,column=0,columnspan=2,sticky="nsew")
label['period_2'].grid(row=2,column=0,sticky="nsew")
label['period_3'].grid(row=2,column=1,sticky="nsew")

window.grid_columnconfigure((0, 1), weight=1)
window.grid_rowconfigure((0, 1, 2), weight=1)
    
window.after(afterTime, update_labels)
window.mainloop()
