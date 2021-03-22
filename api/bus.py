from api.location import convert_to_address
from datetime import time
import os


key = os.environ.get("bing_maps_key")

class BusTrip:
    start_location = None
    end_location = None
    trip = None
    time = None
    eta = None

    def __init__(self, start, end):
        start_location = start
        end_location = end
        if start == None:
            refresh_trip()

    def update_start(self, new_start):
        self.start_location = new_start
        if end_location != None:
            refresh_trip()


    def refresh_trip():
        #TODO Make API all
        #TODO get json
        #TODO yup trip_json - requests.get()
        #TODO extract json Data

