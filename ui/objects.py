class User:

    def __init__(self):
        pass


class Trip:

    def __init__(self):
        pass


class Tripstore:

    def __init__(self):
        pass


class Menu:

    def __init__(self):
        pass

    def sign_up(self):
        pass

    def sign_in(self):
        pass


class Location:

    def __init__(self, city, state, st_address=''):
        self.city = city
        self.state = state
        self.st_address = st_address


class WeatherData:

    def __init__(self, description, temp, wind, weather_id=None, trip_id=None):
        self.desc = description
        self.temp = temp
        self.wind = wind
        self.weather_id = weather_id
        self.trip_id = trip_id
