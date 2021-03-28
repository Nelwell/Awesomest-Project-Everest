from geopy import Nominatim

"""
Module to create Location class.
Holds city, state, St address and converts to lat/lon for API calls
"""


def convert_to_lat_lon(location_address):
    # adapted from https://towardsdatascience.com/geocode-with-python-161ec1e62b89
    locator = Nominatim(user_agent='carless-app')
    location_address = locator.geocode(location_address)
    lat, lon = location_address.latitude, location_address.longitude
    return lat, lon


def convert_to_address(self):
    pass


def convert_to_city(self):
    pass
