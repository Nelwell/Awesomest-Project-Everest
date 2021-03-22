from geopy import Nominatim

"""
Module to create Location class.
Holds city, state, St address and converts to lat/lon for API calls
"""


class Location:

    def __init__(self, city, state, st_address=''):
        self.city = city
        self.state = state
        self.st_address = st_address

    @staticmethod
    def convert_to_lat_lon(address):
        # adapted from https://towardsdatascience.com/geocode-with-python-161ec1e62b89
        locator = Nominatim(user_agent='carless-app')
        location = locator.geocode(f'{address.st_address} '
                                   f'{address.city} '
                                   f'{address.state}')
        lat, lon = location.latitude, location.longitude
        return lat, lon

    def convert_to_address(self):
        pass

    def convert_to_city(self):
        pass
