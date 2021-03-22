import unittest
from api.bus import BusTrip

class BusTripTest(unittest.TestCase):

    def test_new_trip(self):
        newtrip = BusTrip()

    def test_update_time(self):
        #Correctly
        newTime = '3:00:00'
        response = newtrip.update_start_time(newTime)




newtrip = BusTrip('bridge','wharf','2:00:00')

