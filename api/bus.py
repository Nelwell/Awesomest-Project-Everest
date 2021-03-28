from datetime import datetime as dt
import os
import requests
import logging
from requests.models import Response
from validation.validate import *

key = os.environ.get("bing_maps_key")

class BusTrip:
    start_location = None
    end_location = None
    trip = None
    start_time = None
    eta = None
    cost = None
    mode = 'Transit'
    
    
    units = 'imperial'

    def __init__(self, start_location, end_location, start_time):
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
        #TODO Make API all
        #TODO get json
        #TODO yup trip_json - requests.get()
        #TODO extract json Data
        #try:
            
        query = {'travelMode': self.mode, 'waypoint1': self.start_location, 'waypoint2':self.end_location, 'dateTime':self.start_time, 'appid': key}
        #url = f'http://dev.virtualearth.net/REST/v1/Routes/{travelMode}?wayPoint.1={wayPoint1}&viaWaypoint.2={viaWaypoint2}&waypoint.3={waypoint3}&wayPoint.n={waypointN}&heading={heading}&optimize={optimize}&avoid={avoid}&distanceBeforeFirstTurn={distanceBeforeFirstTurn}&routeAttributes={routeAttributes}&timeType={timeType}&dateTime={dateTime}&maxSolutions={maxSolutions}&tolerances={tolerances}&distanceUnit={distanceUnit}&key={BingMapsKey}'
        #url = '%http://dev.virtualearth.net/REST/V1/Routes/Transit?wp.0=Golden%20Gate%20Bridge&wp.1=Fishermans%20Wharf&timeType=Departure&dateTime=3:00:00PM&output=xml&key={key}'
        url = 'http://dev.virtualearth.net/REST/v1/Routes/'
        response = requests.get(url, params=query)
        logging.debug(f'Request sent:\n{response}')
        response.raise_for_status()
        data = response.json()
        if is_valid_json(data):
            logging.info(f'Data recieved:\n{data}')
            return data, None


        #except Exception as e:
        #    logging.exception(e)
        #    logging.exception(response.text)
        #    return None, e

query = {'key': key}
#url = 'http://dev.virtualearth.net/REST/v1/Routes/{travelMode}?wayPoint.1={wayPoint1}&viaWaypoint.2={viaWaypoint2}&waypoint.3={waypoint3}&wayPoint.n={waypointN}&heading={heading}&optimize={optimize}&avoid={avoid}&distanceBeforeFirstTurn={distanceBeforeFirstTurn}&routeAttributes={routeAttributes}&timeType={timeType}&dateTime={dateTime}&maxSolutions={maxSolutions}&tolerances={tolerances}&distanceUnit={distanceUnit}&key={BingMapsKey}'
url = f'%http://dev.virtualearth.net/REST/V1/Routes/Transit?wp.0=Golden%20Gate%20Bridge&wp.1=Fishermans%20Wharf&timeType=Departure&dateTime=3:00:00PM&output=xml&key={key}'
url = 'http://dev.virtualearth.net/REST/v1/Routes'
response = requests.get(url, params=query)
print(type(response))
# logging.debug(f'Request sent:\n{response}')
# response.raise_for_status()
# data = response.json()
# logging.info(f'Data recieved:\n{data}')

# print(data)