import time
from gps3.agps3threaded import AGPS3mechanism
from dotenv import load_dotenv
import os
import redis
import json
load_dotenv(".env")

class GPS:
    def __init__(self):
        self.agps_thread = AGPS3mechanism()
        self.agps_thread.stream_data()
        self.agps_thread.run_thread()
        self.realData = False
        self.update()
    
    def update(self):
        startTime = time.time()
        while self.time() == "n/a" and time.time() - startTime < 10:
            time.sleep(0.2)
            # print(time.time() - startTime )
        if self.time() != "n/a":
            self.realData = True
            # self.print_gps_data()
        else:
            print ("Timed out after 10 seconds. Error loading gps data")
        

    def print_gps_data(self):
        data = self.agps_thread.data_stream
        print('---------------------')
        print(f'Time: {data.time}')
        print(f'Lat: {data.lat}')
        print(f'Lon: {data.lon}')
        print(f'Speed: {data.speed}')
        print(f'Course: {data.track}')
        print('---------------------')

    def time(self):
        return str(self.agps_thread.data_stream.time)

    def lat(self):
        return str(self.agps_thread.data_stream.lat)

    def lon(self):
        return str(self.agps_thread.data_stream.lon)

    def status(self):
        return str(self.agps_thread.data_stream.status)
        
    def time_offset(self):
        return str(self.agps_thread.data_stream.ept)

    def speed(self):
        return str(self.agps_thread.data_stream.speed)

    def alt(self):
        return str(self.agps_thread.data_stream.alt)

    def saveToDatabase(self):
        data = self.agps_thread.data_stream
        c = 0
        while True:
            if data.time == "n/a":
                c += 1
                if c > 100:
                    quit()
                sleep(.1)
            else:
                break
        print('---------------------')
        print(f'Time: {data.time}')
        print(f'Lat: {data.lat}')
        print(f'Lon: {data.lon}')
        print(f'Speed: {data.speed}')
        print(f'Course: {data.track}')
        print('---------------------')
        r = redis.Redis(db=0,host=os.getenv("redis_database_name"),port=os.getenv("redis_database_port"),password=os.getenv("redis_database_password"))
        My_location = {
            'Time' : data.time,
            'Lat' : data.lat,
            'Lon': data.lon,
            'Speed': data.speed,
            'Course': data.track
        }

        My_location_json_string = json.dumps(My_location)
        try:
            result = r.set('My_location',My_location_json_string)
            print("database updated")
        except:
            print(f"error writing to the database: {redis_database_name}")
        print('---------------------')
        
        filename = ".My_location.json"
        try:
            with open(filename, "w") as file:
                json.dump(My_location, file, indent=4)
            print(f"location saved to disk at {filename}")
        except:
            print(f"error writing to file {filename}")
        print('---------------------')


if __name__ == "__main__":
    try:
        myGPS = GPS()
        # myGPS.print_gps_data()
        myGPS.saveToDatabase()

    except Exception as e:
        print(f"An error occurred: {e}")