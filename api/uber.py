import requests
import time
from validate import is_valid_json


class UberError(Exception):
	pass


class UberTrip:
	start_lat = None
	start_lon = None
	end_lat = None
	end_lon = None
	trip_time = None
	price = None
	duration = None
	distance = None

	def __init__(self, start_lat, start_lon, end_lat, end_lon, trip_time=time.strftime("%H:%M:%S",time.localtime())):
		self.start_lat = start_lat
		self.start_lon = start_lon
		self.end_lat = end_lat
		self.end_lon = end_lon
		self.trip_time = trip_time

		self.call_api()


	def __str__(self):
		return f'start lat, lon: {self.start_lat}, {self.start_lon}\nend lat, lon: {self.end_lat}, {self.end_lon}\ntrip time: {self.trip_time}\nprice: {self.price}\nduration: {self.duration}\ndistance: {self.distance}'


	def call_api(self):
		# only works when flask test environment is running
		query = {'start_latitude': self.start_lat, 'start_longitude': self.start_lon, 'end_latitude': self.end_lat, 'end_longitude': self.end_lon, 'time': self.trip_time}
		url = 'http://127.0.0.1:5000/v1.2/estimates/price'
		data = requests.get(url,params=query).json()
		self.parse_data(data)
		# if is_valid_json(data):
		# 	self.parse_data(data)
		# else:
		# 	raise UberError('Invalid JSON.')


	def parse_data(self, uber_trip_details):
		try:
			details = []
			for item in uber_trip_details:
				if item['display_name'] == "uberX":
					self.price = round(((float(item['low_estimate']) + float(item['high_estimate'])) / 2),2)	# average of high and low
					self.duration = self.calculate_duration(float(item['duration']))
					self.distance = float(item['distance'])
		except KeyError:
			raise UberError('Invalid selection.')


	def calculate_duration(self, duration):
		modifier = 60	# seconds in a minute, minutes in an hour
		seconds = duration % modifier ** 1
		remainder = duration - seconds
		minutes = remainder % modifier ** 2
		hours = (duration - minutes) - seconds
		hours = hours / modifier / modifier
		minutes = minutes / modifier

		new_time = f'{int(hours)}:{int(minutes)}:{int(seconds)}'

		return new_time
