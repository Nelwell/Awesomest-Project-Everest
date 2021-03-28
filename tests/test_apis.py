import unittest
from api.bus import *

class BusTripTest(unittest.TestCase):

    def test_foo(self):
        stringTest = "variable"
        response = foo(stringTest)

    def test_new_trip(self):
        start_loc = "Golden Gate Bridge"
        end_loc = "Fisherman's Wharf"
        start_time = dt.now()
        response = BusTrip(start_loc,end_loc,start_time)

    def test_update_time(self):
        #Correctly
        newTime = '3:00:00'
        response = newtrip.update_start_time(newTime)




# newtrip = BusTrip('bridge','wharf','2:00:00')

