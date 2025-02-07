import time
from gps3.agps3threaded import AGPS3mechanism
class GPS:
    def __init__(self):
        # from time import sleep
        self.agps_thread = AGPS3mechanism()  # Instantiate AGPS3 Mechanisms
        self.agps_thread.stream_data()  # From localhost (), or other hosts, by example, (host='gps.ddns.net')
        self.agps_thread.run_thread()  # Throttle time to sleep after an empty lookup, default '()' 0.2 two tenths of a second
    
    def update(self):
        print('---------------------')
        print('Time:{}  '.format(self.agps_thread.data_stream.time))
        print('Lat:{}   '.format(self.agps_thread.data_stream.lat))
        print('Lon:{}   '.format(self.agps_thread.data_stream.lon))
        print('Speed:{} '.format(self.agps_thread.data_stream.speed))
        print('Course:{}'.format(self.agps_thread.data_stream.track))
        print('---------------------')
    
    def time(self):
        return self.agps_thread.data_stream.time

    def lat(self):
        return self.agps_thread.data_stream.lat

    def lon(self):
        return self.agps_thread.data_stream.lon

    def status(self):
        return self.agps_thread.data_stream.status

    def timeOffset(self):
        return self.agps_thread.data_stream.ept

    def speed(self):
        return self.agps_thread.data_stream.speed

    def alt(self):
        return self.agps_thread.data_stream.alt

if __name__ == "__main__":
    myGPS = GPS()
    time.sleep(2)
    myGPS.update()
