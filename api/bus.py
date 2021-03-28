from datetime import datetime as dt
import os
import requests
import logging
from requests.models import Response
#from ..validation.validate import *

key = os.environ.get("bing_maps_key")

# def foo(bar):
#     if (len(bar) > 1):
#         print(bar)

class BusTrip:
    start_location = None
    end_location = None
    trip = None
    start_time = None
    eta = None
    cost = None
    mode = 'Transit'
    
    
    units = 'imperial'

    def __init__(self, start_location, end_location, start_time): #Format: "Golden Gate Bridge", "Fisherman's Wharf", '05:42:00'
        if start_location != None and end_location != None and start_time !=None:
            self.start_location = start_location
            self.end_location = end_location
            self.start_time = start_time
            self.refresh_trip()
        
    def __str__(self) -> str:
        return f'Start: {self.start_location} End: {self.end_location} Time: {self.time} Cost: {self.cost}'

    def update_start(self, new_location):
        self.start_location = new_location
        if self.start_location != None:
            self.refresh_trip()

    def update_start_time(self, new_time):
        self.start_time = new_time
        self.refresh_trip()

    def update_end(self, new_location):
        self.end_location = new_location
        if self.end_location != None:
            self.refresh_trip()

    def refresh_trip(self):
        #TODO extract json Data
        try:
            print(self.start_location, self.end_location, self.start_time)
            query = {'travelMode': self.mode, 'waypoint.1': self.start_location, 'waypoint.2':self.end_location, 'dateTime':self.start_time, 'key': key}
            url = 'http://dev.virtualearth.net/REST/v1/Routes/'
            print(requests.get(url, params=query))
            response = requests.get(url, params=query)
            print(f'Request sent:\n{response}')
            response.raise_for_status()
            data = response.json()
            logging.info(f'Data recieved:\n{data}')
            print(data)
            # if is_valid_json(data):
            #     logging.info(f'Data recieved:\n{data}')
            #     return data, None


        except Exception as e:
           logging.exception(e)
           logging.exception(response.text)
           return None, e

# print(data)
var = BusTrip("Golden Gate Bridge", "Fisherman's Wharf", '05:42:00')