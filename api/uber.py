class UberTrip():
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


	def __str__(self):
		return f'start lat, lon: {self.start_lat}, {self.start_lon}\nend lat, lon: {self.end_lat}, {self.end_lon}\ntrip time: {self.trip_time}\nprice: {self.price}\nduration: {self.duration}\ndistance: {self.distance}'
