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
    latitude = myGPS.lat
    longitude = myGPS.lon
    weatherURL = "https://api.weather.gov/points/{latitude},{longitude}"
    print (weatherURL)
    response = urlopen(weatherURL) 
    data_json = json.loads(response.read()) 
    print(data_json) 