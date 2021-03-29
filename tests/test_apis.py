import unittest
import json
from api.bus import *
from validate  import *

class BusTripTest(unittest.TestCase):

    def test_new_trip(self):
        start_loc = "Mall of America"
        end_loc = "Target Field"
        start_time = '08:45:00'
        response = BusTrip(start_loc,end_loc,start_time)
        self.assertTrue(type(response) == BusTrip)

    # def test_update_time(self):
    #     #Correctly
    #     newTime = '3:00:00'
    #     response = newtrip.update_start_time(newTime)

    def test_convert_time(self):
        epoch_timestamp = '/Date(1616950606000-0700)/'
        expected_result = dt(2021,3,28,11,56,46)
        response = convert_time(epoch_timestamp)
        self.assertTrue(response == expected_result)

    def test_extract_json(self):
        #Test proper extraction of data from json file
        #This test duplicates the code of the method and does not actually implement it.
        with open('tests/test.json') as test_json:
            test_trip = json.load(test_json)
        test_cost = 0
        response = test_trip['resourceSets'][0]['resources'][0]['routeLegs'][0]['cost']
        self.assertEqual(test_cost,response,f"This test was expecting {test_cost} but recieved {response}")
        
        test_duration = 3101
        response = test_trip['resourceSets'][0]['resources'][0]['travelDuration']
        self.assertEqual(test_duration,response,f"This test was expecting {test_duration} but recieved {response}")
      
        test_distance = 8.305
        response = test_trip['resourceSets'][0]['resources'][0]['travelDistance']
        self.assertEqual(test_distance,response,f"This test was expecting {test_distance} but recieved {response}")

        test_start_time = "/Date(1616883467000-0700)/"
        response = test_trip['resourceSets'][0]['resources'][0]['routeLegs'][0]['startTime']
        self.assertEqual(test_start_time,response,f"This test was expecting {test_start_time} but recieved {response}")

        test_eta = "/Date(1616886568000-0700)/"
        response = test_trip['resourceSets'][0]['resources'][0]['routeLegs'][0]['endTime']
        self.assertEqual(test_eta,response,f"This test was expecting {test_eta} but recieved {response}")

        test_start_coordinates = [37.812166,-122.477803]
        response = test_trip['resourceSets'][0]['resources'][0]['routeLegs'][0]['actualStart']['coordinates']
        self.assertEqual(test_start_coordinates,response,f"This test was expecting {test_start_coordinates} but recieved {response}.")

        test_end_coordinates = [37.808211,-122.415805]
        response = test_trip['resourceSets'][0]['resources'][0]['routeLegs'][0]['actualEnd']['coordinates']
        self.assertEqual(test_end_coordinates,response,f"This test was expecting {test_end_coordinates} but recieved {response}.")