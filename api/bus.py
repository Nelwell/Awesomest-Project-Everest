from datetime import datetime as dt
import os
import requests
import logging
from requests.models import Response
from validate import *
from api.validate import is_valid_json


key = os.environ.get("bing_maps_key")

class BusTrip:
    #hardcoded data
    mode = 'Transit'
    units = 'imperial'

    #Set on creation
    start_location = None
    end_location = None
    start_time = None


    #Set on data conversion from json to BusTrip object
    trip = None
    trip_start_time = None
    eta = None
    cost = None
    start_coordinates = None
    end_coordinates = None
    duration = None
    distance = None    

    #Set start and end location and requested start time in init
    def __init__(self, start_location, end_location, start_time): #Format: "Golden Gate Bridge", "Fisherman's Wharf", '05:42:00'
        if start_location != None and end_location != None and start_time !=None:
            self.start_location = start_location
            self.end_location = end_location
            self.start_time = start_time
            self.refresh_trip()
        
    def __str__(self) -> str:
        return f'Start: {self.start_location}, End: {self.end_location}, Duration: {self.duration}, Arrival time: {self.eta}, Cost: {self.cost}'

    #allows trip to be recreated using new start location
    def update_start(self, new_location):
        self.start_location = new_location
        if self.start_location != None:
            self.refresh_trip()

    #allows trip to be recreated using new start time
    def update_start_time(self, new_time):
        self.start_time = new_time
        self.refresh_trip()

    #allows trip to be recreated using new end location
    def update_end(self, new_location):
        self.end_location = new_location
        if self.end_location != None:
            self.refresh_trip()


    #Transfers data from json to BusTrip object
    def extract_json(self, data):
        self.trip = data
        self.cost = self.trip['resourceSets'][0]['resources'][0]['routeLegs'][0]['cost']
        self.trip_start_time = self.trip['resourceSets'][0]['resources'][0]['routeLegs'][0]['startTime']
        self.eta = self.trip['resourceSets'][0]['resources'][0]['routeLegs'][0]['endTime']
        self.start_coordinates = self.trip['resourceSets'][0]['resources'][0]['routeLegs'][0]['actualStart']['coordinates']
        self.end_coordinates = self.trip['resourceSets'][0]['resources'][0]['routeLegs'][0]['actualEnd']['coordinates']
        self.duration = self.trip['resourceSets'][0]['resources'][0]['travelDuration']
        self.distance = self.trip['resourceSets'][0]['resources'][0]['travelDistance']


    #Pulls JSON of trip from bing.
    def refresh_trip(self):
        try:
            query = {'travelMode': self.mode, 'waypoint.1': self.start_location, 'waypoint.2':self.end_location, 'dateTime':self.start_time, 'key': key}
            url = 'http://dev.virtualearth.net/REST/v1/Routes/'
            response = requests.get(url, params=query)
            response.raise_for_status()
            data = response.json()

            #Uses json validator
            if is_valid_json(data):
                logging.info(f'Data recieved:\n{data}')
                self.extract_json(data)
        except Exception as e:
           logging.exception(e)
           logging.exception(response.text)
           return None, e

trip = BusTrip("Mall of America", "Target Field", "9:00:00")

pass

print(trip)
