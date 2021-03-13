import sqlite3
from db_config import DATABASE


def setup_database():
	'''The three tables are users: storing base information about users; credentials: storing
	 information to authenticate within the application; and trips: storing api data about
	 trips user decides to bookmark.'''
	
	'''Username column is used for signing in, and providing foreign key to cred and trip
	 tables. Name column is used for printing meaningful messages to the user.'''
	create_sql = 'CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, username TEXT UNIQUE NOT NULL, name TEXT)'
	create_table(create_sql)

	'''Username acts as foreign key from users table; email address acts as alternate form of
	 authentication on sign in; password is stored as SHA-256 hashed value of password; salt is
	 stored to apply to password before hashing to entered password to verify stored encrypted
	 password and entered passwords match.'''
	'''NOT NULL constraint not listed under email_address for the case the user only wished to
	 provide one method of verification.'''
	create_sql = 'CREATE TABLE IF NOT EXISTS credentials (credential_id INTEGER PRIMARY KEY, ' \
				 'username TEXT UNIQUE NOT NULL, email_address TEXT UNIQUE COLLATE NOCASE, ' \
				 'password TEXT UNIQUE NOT NULL, salt TEXT UNIQUE NOT NULL, ' \
				 'FOREIGN KEY(username) REFERENCES users(username))'
	create_table(create_sql)

	'''Username acts as a foreign key from users table; trip_start_time is time user called, or
	 planned from their ride; start/end lat/long columns are the location start and end points;
	 price is estimate gained from uber, or calculated value based on distance from transit;
	 is_transit is a boolean value determining if ride share or public transit.'''
	'''NOT NULL constraints not listed under start time and location, price, or is_transit for
	 the case the user is saving a favorite route, not interesting result, e.g. going to a close
	 friends.'''
	create_sql = 'CREATE TABLE IF NOT EXISTS trips (trip_id INTEGER PRIMARY KEY, username TEXT NOT NULL, ' \
				 'trip_start_time DATETIME, trip_start_lat DECIMAL, trip_start_long DECIMAL, ' \
				 'trip_stop_lat DECIMAL NOT NULL, trip_stop_long DECIMAL NOT NULL, price DECIMAL, is_transit BOOLEAN, ' \
				 'FOREIGN KEY(username) REFERENCES users(username))'
	create_table(create_sql)

	'''Either this, or the previous create_sql strings and create_table calls should be commented
	 out, depending on whether or not lat/long is used, or if lat/long and address is needed,
	 based on whichever conversion is easier.'''

	'''Username acts as a foreign key from users table; trip_start_time is time user called, or
	 planned from their ride; start/end address columns are the location start and end points;
	 price is estimate gained from uber, or calculated value based on distance from transit;
	 is_transit is a boolean value determining if ride share or public transit.'''
	'''NOT NULL constraints not listed under start time and location, price, or is_transit for
	 the case the user is saving a favorite route, not interesting result, e.g. going to a close
	 friends.'''
	create_sql = 'CREATE TABLE IF NOT EXISTS trips (trip_id INTEGER PRIMARY KEY, username TEXT NOT NULL, ' \
				 'trip_start_time DATETIME, trip_start_address TEXT, trip_start_city TEXT, trip_start_state TEXT, ' \
				 'trip_stop_address TEXT NOT NULL, trip_stop_city TEXT NOT NULL, trip_stop_state TEXT NOT NULL, ' \
				 'price DECIMAL, is_transit BOOLEAN, FOREIGN KEY(username) REFERENCES users(username))'
	create_table(create_sql)

	'''Trip_id acts as a foreign key from users table; temperature is temperature X amount of
	 minutes after start time of trip; description is a text value of weather, e.g. cloudy,
	 raining, snowing.'''
	'''NOT NULL constraints not listed under temperature and description for the case the api
	 returns None for that location and time. Constraint should be placed if check is made
	 elsewhere to prevent this.'''
	create_sql = 'CREATE TABLE IF NOT EXISTS weather_details (weather_id INTEGER PRIMARY KEY, trip_id INTEGER NOT NULL, ' \
				 'temperature_f DECIMAL, description TEXT, FOREIGN KEY(trip_id) REFERENCES trips(trip_id))'
	create_table(create_sql)


def create_table(create_sql):
	with sqlite3.connect(DATABASE) as connection:
		connection.execute(create_sql)
	connection.close()


def create_row():
	pass


def read_row():
	pass


def update_row():
	pass


def delete_row():
	pass


setup_database()
