from geopy import Nominatim

"""
Remove lines 8-11 and 38 before approving/merging to main branch, as well as this docstring comment.
"""


def main():
    address = Location('Minneapolis', 'MN', '1501 Hennepin Ave')  # example location object, MCTC address
    lat, long = Location.convert_to_lat_long(address)  # pass examples to method to convert to lat/long
    print(f'Test Latitude = {lat}, Test Longitude = {long}')  # for testing


class Location:

    def __init__(self, city, state, st_address=''):
        self.city = city
        self.state = state
        self.st_address = st_address

    @staticmethod
    def convert_to_lat_long(address):
        # adapted from https://towardsdatascience.com/geocode-with-python-161ec1e62b89
        locator = Nominatim(user_agent='carless-app')
        location = locator.geocode(f'{address.st_address} '
                                   f'{address.city} '
                                   f'{address.state}')
        lat, long = location.latitude, location.longitude
        return lat, long

    def convert_to_address(self):
        pass

    def convert_to_city(self):
        pass


main()
