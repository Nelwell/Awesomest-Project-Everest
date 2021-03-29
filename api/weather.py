import os
import requests
from datetime import datetime

wx_key = os.environ.get('open_weather_key')  # environment variable
query = {'lat': 44.972659, 'lon': -93.28372334243436, 'units': 'imperial', 'appid': wx_key}  # dictionary to store params
url = 'http://api.openweathermap.org/data/2.5/forecast'  # base url


def get_weather_data(start_lat, start_lon, end_lat, end_lon, start_address, end_address):
    # start_lat, start_lon, end_lat, end_lon, start_address, end_address = get_locations()
    start_weather_data, end_weather_data, error = get_wx_json(start_lat, start_lon, end_lat, end_lon, wx_key)
    if error:
        print('Sorry, could not get weather for that location or location doesn\'t exist')
    else:
        display_wx_forecast(start_weather_data, end_weather_data, start_address, end_address)
    return start_weather_data, end_weather_data


# def get_locations():
#     start_st_address, start_city, start_state = '', '', ''
#     end_st_address, end_city, end_state = '', '', ''
#     while len(start_st_address) == 0:
#         start_st_address = input('Enter the departure street address: ').title().strip()
#
#     while len(start_city) == 0:
#         start_city = input('Enter departure the city: ').title().strip()
#
#     while len(start_state) != 2 or not start_state.isalpha():
#         start_state = input('Enter the 2-letter departure state abbreviation: ').upper().strip()
#
#     while len(end_st_address) == 0:
#         end_st_address = input('Enter the destination street address: ').title().strip()
#
#     while len(end_city) == 0:
#         end_city = input('Enter destination the city: ').title().strip()
#
#     while len(end_state) != 2 or not end_state.isalpha():
#         end_state = input('Enter the 2-letter destination state abbreviation: ').upper().strip()
#
#     start_address = f'{start_st_address}, {start_city}, {start_state}'
#     end_address = f'{end_st_address}, {end_city}, {end_state}'
#     start_lat, start_lon = location.convert_to_lat_lon(start_address)  # pass start address to lat/lon conversion function
#     end_lat, end_lon = location.convert_to_lat_lon(end_address)  # same for end address
#     return start_lat, start_lon, end_lat, end_lon, start_address, end_address


def get_wx_json(start_lat, start_lon, end_lat, end_lon, wx_key):
    try:
        # start location weather data
        start_query = {'lat': start_lat, 'lon': start_lon, 'units': 'imperial', 'appid': wx_key}
        start_response = requests.get(url, params=start_query)
        start_response.raise_for_status()  # Raise exception for 400 or 500 errors
        start_wx_data = start_response.json()  # this

        # end location weather data
        end_query = {'lat': end_lat, 'lon': end_lon, 'units': 'imperial', 'appid': wx_key}
        end_response = requests.get(url, params=end_query)
        end_response.raise_for_status()  # Raise exception for 400 or 500 errors
        end_wx_data = end_response.json()  # this may error too, if response is not JSON

        return start_wx_data, end_wx_data, None
    except Exception as e:
        return None, e


def display_wx_forecast(start_weather_data, end_weather_data, start_address, end_address):
    start_fcst_data_list = start_weather_data['list']

    for element in start_fcst_data_list:
        temp = element['main']['temp']
        wind_spd = element['wind']['speed']
        timestamp = element['dt']
        valid_datetime = datetime.utcfromtimestamp(timestamp)
        print(f'\nAt {valid_datetime}UTC:\n'
              f'\tTemperature: {temp}°F')
        wx_desc_list = element['weather']
        for wx in wx_desc_list:
            wx_desc = wx['description']
            print(f'\tWeather: {wx_desc}')
        print(f'\tWind Speed: {wind_spd}mph')
