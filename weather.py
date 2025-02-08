from urllib.request import urlopen 
import json 
import gps
import time
  
# store the response of URL 
  
# storing the JSON response  
# from url in data 
  
# print the json response 

if __name__ == "__main__":
    myGPS = gps.GPS()
    time.sleep(2)
    myGPS.update()
    # weatherURL = "https://api.weather.gov/points/{latitude},{longitude}".format(latitude = myGPS.lat,longitude = myGPS.lon)
    while True:
        weatherURL = 'https://api.weather.gov/points/{latitude},{longitude}'.format(latitude = myGPS.lat(),longitude = myGPS.lon())
        if weatherURL != "https://api.weather.gov/points/n/a,n/a":
            break
    # 'Number {0}: {1:{2}.2f}'.format(i, num, field_size)
    # 'Number {i}: {num:{field_size}.2f}'.format(i=i, num=num, field_size=field_size)


    print (weatherURL)
    print ()
    response = urlopen(weatherURL) 
    data_json = json.loads(response.read()) 
    newURL = data_json['properties']['forecast']
    print(newURL)
    print ()
    response = urlopen(newURL) 
    data_json = json.loads(response.read()) 
    secondNewURL = data_json['properties']['periods']
    print(secondNewURL[0]['name'],": ",secondNewURL[0]['shortForecast'])
    print("Temperature: ",secondNewURL[0]['temperature'],secondNewURL[0]['temperatureUnit'])
    print("Wind: ",secondNewURL[0]['windSpeed'],secondNewURL[0]['windDirection'])
    print("Details: ",secondNewURL[0]['windSpeed'])

    print ()
    # print(secondNewURL[1])
    # print ()
