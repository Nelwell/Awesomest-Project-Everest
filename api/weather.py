import os
import requests
from datetime import datetime
import location

wx_key = os.environ.get('open_weather_key')  # environment variable
query = {'lat': 44.972659, 'lon': -93.28372334243436, 'units': 'imperial', 'appid': wx_key}  # dictionary to store params
url = 'http://api.openweathermap.org/data/2.5/forecast'  # base url


def get_weather_data():
    lat, lon, location_address = get_location()
    # start_datetime, stop_datetime = get_datetimes()
    weather_data, error = get_wx_json(lat, lon, wx_key)
    if error:
        print('Sorry, could not get weather for that location or location doesn\'t exist')
    else:
        display_wx_forecast(weather_data, location_address)
    return weather_data


def get_location():
    st_address, city, state = '', '', ''
    while len(st_address) == 0:
        st_address = input('Enter the street address: ').title().strip()

    while len(city) == 0:
        city = input('Enter the city: ').title().strip()

    while len(state) != 2 or not state.isalpha():
        state = input('Enter the 2-letter state abbreviation: ').upper().strip()

    location_address = f'{st_address}, {city}, {state}'
    lat, lon = location.convert_to_lat_lon(location_address)  # pass address to lat/lon conversion function
    return lat, lon, location_address


# def get_datetimes():
    


def get_wx_json(lat, lon, wx_key):
    try:
        query = {'lat': lat, 'lon': lon, 'units': 'imperial', 'appid': wx_key}
        response = requests.get(url, params=query)
        response.raise_for_status()  # Raise exception for 400 or 500 errors
        data = response.json()  # this may error too, if response is not JSON
        return data, None
    except Exception as e:
        return None, e


def display_wx_forecast(weather_data, location_address):
    fcst_data_list = weather_data['list']

    print(f'\n*** HERE\'S YOUR {location_address} 3-HOURLY, 5-DAY FORECAST ***')
    for element in fcst_data_list:
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


get_weather_data()