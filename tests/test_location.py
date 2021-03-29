import unittest
from unittest import TestCase
from api import location


class TestLatLonConverter(TestCase):

    def test_convert_address_to_lat_lon(self):
        # Arrange
        example_address = '1501 Hennepin Ave', 'Minneapolis', 'MN'
        actual_lat, actual_lon = 44.972659, -93.28372334243436  # MCTC lat/lon

        # Action - runs example address through conversion method
        expected_lat, expected_lon = location.convert_to_lat_lon(example_address)

        # Assert - checks actual lat/lon matches converted lat/lon of example address
        self.assertEqual((expected_lat, expected_lon), (actual_lat, actual_lon))


if __name__ == '__main__':
    unittest.main()
