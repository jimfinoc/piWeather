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
    weatherURL = 'https://api.weather.gov/points/{latitude},{longitude}'.format(latitude = myGPS.lat(),longitude = myGPS.lon())
    # 'Number {0}: {1:{2}.2f}'.format(i, num, field_size)
    # 'Number {i}: {num:{field_size}.2f}'.format(i=i, num=num, field_size=field_size)


    print (weatherURL)
    print ()
    response = urlopen(weatherURL) 
    data_json = json.loads(response.read()) 
    print(data_json[properties['forecast']]) 