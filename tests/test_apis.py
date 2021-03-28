import unittest
import json
from api.bus import *
from validate  import *

class BusTripTest(unittest.TestCase):

    def test_new_trip(self):
        start_loc = "Golden Gate Bridge"
        end_loc = "Fisherman's Wharf"
        start_time = '05:42:00'
        response = BusTrip(start_loc,end_loc,start_time)
        self.assertTrue(type(response) == BusTrip)

    # def test_update_time(self):
    #     #Correctly
    #     newTime = '3:00:00'
    #     response = newtrip.update_start_time(newTime)

    def test_extract_json(self):
        #Test proper extraction of data from json file
        with open('tests/test.json') as test_json:
            test_trip = json.load(test_json)
        test_cost = 0
        response = test_trip['resourceSets'][0]['resources'][0]['routeLegs'][0]['cost']
        self.assertIs(test_cost,response,"This test was expecting {test_cost} but recieved {response}.")
        # test_trip.cost = test_trip.trip['resourceSets']['resources']['routeLegs'][0]['cost']
        # test_trip.trip_start_time = test_trip.trip['resourceSets'][0]['resources'][0]['routeLegs'][0]['cost']
        # test_trip.eta = test_trip.trip['resourceSets'][0]['resources'][0]['routeLegs'][0]['cost']
        # test_trip.cost = test_trip.trip['resourceSets'][0]['resources'][0]['routeLegs'][0]['cost']
        # test_trip.start_coordinates = test_trip.trip['resourceSets'][0]['resources'][0]['routeLegs'][0]['cost']
        # test_trip.end_coordinates = test_trip.trip['resourceSets'][0]['resources'][0]['routeLegs'][0]['cost']
        # test_trip.duration = test_trip.trip['resourceSets'][0]['resources'][0]['routeLegs'][0]['cost']
        # test_trip.distance = test_trip.trip['resourceSets'][0]['resources'][0]['routeLegs'][0]['cost']




