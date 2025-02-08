import time
from gps3.agps3threaded import AGPS3mechanism

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

if __name__ == "__main__":
    try:
        myGPS = GPS()
        myGPS.print_gps_data()
    except Exception as e:
        print(f"An error occurred: {e}")