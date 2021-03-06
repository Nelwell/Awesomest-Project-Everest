import sqlite3
from db_config import DATABASE


# seconds_since_epoch = dt.now()
# trip_start_eta = input('How many minutes from now do you want to leave?')
# trip_start_time = seconds_since_epoch + (trip_start_eta * 60)
# time_api_can_read = some_conversion(trip_start_time)


class DatabaseManager:
	
	def __init__(self):
		"""The three tables are users: storing base information about users; credentials: storing information
		to authenticate within the application; and trips: storing api data about trips user decides to bookmark."""

		"""Username column is used for signing in, and providing foreign key to cred and trip tables. 
		Name column is used for printing meaningful messages to the user."""
		create_users_sql = 'CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, username TEXT UNIQUE NOT NULL, name TEXT)'

		"""Username acts as foreign key from users table; email address acts as alternate form of 
		authentication on sign in; password is stored as SHA-512 hashed value of password; salt is 
		stored to apply to password before hashing to entered password to verify stored encrypted 
		password and entered passwords match."""
		"""NOT NULL constraint not listed under email_address for the case the user only wishes to 
		provide one method of verification."""
		create_credentials_sql = 'CREATE TABLE IF NOT EXISTS credentials (credential_id INTEGER PRIMARY KEY, ' \
					 'username TEXT UNIQUE NOT NULL, email_address TEXT UNIQUE COLLATE NOCASE, ' \
					 'password TEXT UNIQUE NOT NULL, salt TEXT UNIQUE NOT NULL, ' \
					 'FOREIGN KEY(username) REFERENCES users(username))'

		"""Username acts as a foreign key from users table; trip_start_time is time user plans to depart for trip; 
		start/end lat/long columns are the location start and end points; 
		price is estimate gained from uber, or calculated value based on distance from transit; 
		is_transit is a boolean value determining if ride share or public transit."""
		"""NOT NULL constraints not listed under start time and location, price, or is_transit for 
		the case the user is saving a favorite route, not interesting result, e.g. going to a close friend's."""
		create_trips_sql = 'CREATE TABLE IF NOT EXISTS trips (trip_id INTEGER PRIMARY KEY, username TEXT NOT NULL, ' \
					 'trip_start_time DATETIME, trip_start_lat DECIMAL, trip_start_long DECIMAL, ' \
					 'trip_stop_lat DECIMAL NOT NULL, trip_stop_long DECIMAL NOT NULL, price DECIMAL, is_transit BOOLEAN, ' \
					 'FOREIGN KEY(username) REFERENCES users(username))'

		# """Either this, or the previous create_sql strings and create_table calls should be commented
		#  out, depending on whether or not lat/long is used, or if lat/long and address is needed,
		#  based on whichever conversion is easier."""
		#
		# """Username acts as a foreign key from users table; trip_start_time is time user called, or
		#  planned from their ride; start/end address columns are the location start and end points;
		#  price is estimate gained from uber, or calculated value based on distance from transit;
		#  is_transit is a boolean value determining if ride share or public transit."""
		# """NOT NULL constraints not listed under start time and location, price, or is_transit for
		#  the case the user is saving a favorite route, not interesting result, e.g. going to a close
		#  friends."""
		# create_sql = 'CREATE TABLE IF NOT EXISTS trips (trip_id INTEGER PRIMARY KEY, username TEXT NOT NULL, ' \
		# 			 'trip_start_time DATETIME, trip_start_address TEXT, trip_start_city TEXT, trip_start_state TEXT, ' \
		# 			 'trip_stop_address TEXT NOT NULL, trip_stop_city TEXT NOT NULL, trip_stop_state TEXT NOT NULL, ' \
		# 			 'price DECIMAL, is_transit BOOLEAN, FOREIGN KEY(username) REFERENCES users(username))'
		# create_table(create_sql)

		"""Trip_id acts as a foreign key from trips table; 
		temperature is forecast temperature for trip start/end times and locations; 
		wind speed is forecast wind speed for trip start/end times and locations;
		description is text description of forecast weather for trip start/end times and locations, e.g. cloudy, rain, snow."""
		"""NOT NULL constraints not listed under temperature, wind speed and description for the case the api returns None 
		for that time and location. Constraint should be placed if check is made elsewhere to prevent this."""
		create_wx_sql = 'CREATE TABLE IF NOT EXISTS weather_details (weather_id INTEGER PRIMARY KEY, ' \
						'trip_id INTEGER NOT NULL, start_temperature DECIMAL, stop_temperature DECIMAL, ' \
						'start_wind_spd INTEGER, stop_wind_spd INTEGER, start_description TEXT, stop_description TEXT, ' \
						'FOREIGN KEY(trip_id) REFERENCES trips(trip_id))'

		tables = [create_users_sql, create_credentials_sql, create_trips_sql, create_wx_sql]  # list of db tables
		self.create_table(tables)


	def create_table(self,tables):
		enable_fk = 'PRAGMA foreign_keys = ON'

		with sqlite3.connect(DATABASE) as connection:
			connection.execute(enable_fk)  # ensures foreign key support is enabled in older versions of Python
			for table in tables:
				connection.execute(table)
		connection.close()


	'''Create Row method should be sent a string of the table to be modified, a list of strings for each column, and
	 a list of strings for the values corresponding to each column.'''
	def create_row(self,table,columns,values):
		insert = self.get_insert_statement(table,columns,values)
		creation_tuple = self.get_creation_tuple(values)
		with sqlite3.connect(DATABASE) as connection:
			connection.execute(insert, creation_tuple)
		connection.close()


	'''This method takes the columns from the method it's called by to create a string to use for sql insertion.'''
	def get_insert_statement(self,table,columns,values):
		insert = f'INSERT INTO {table} ('
		for i in range(len(columns)):
			insert = insert + columns[i]
			if i < len(columns) - 1:
				insert = insert + ', '
		insert = insert + ')'
		insert_buffer = ', ?'*(len(values)-1)
		insert = f'{insert} values (?{insert_buffer})'

		return insert


	'''Return a tuple of a string. Pretty simple. Sure, yeah.'''
	def get_creation_tuple(self,values):
		return tuple(values)


	'''Method should be sent string values of table to update, key and value.'''
	def read_row(self, table, key, value, rows='*'):
		results = []

		select = f'SELECT {rows} FROM {table} WHERE {key} = ?'
		connection = sqlite3.connect(DATABASE)
		rows = connection.execute(select, (value,))
		for row in rows:
			results.append(row)
		connection.close()
		return results


	'''Method should be sent string values of table to update, column to check, column to update, value to check, and
	 value to update.'''
	def update_row(self, table, where_column, set_column, where_value, set_value):
		with sqlite3.connect(DATABASE) as connection:
			update = f'UPDATE {table} SET {set_column} = ? WHERE {where_column} = ?'
			connection.execute(update, (set_value,where_value))
		connection.close()


	'''Method should be sent string values of table to update, column to check, and value to check for.'''
	def delete_row(self, table, delete_column, delete_value):
		with sqlite3.connect(DATABASE) as connection:
			delete = f'DELETE FROM {table} WHERE {delete_column} = ?'
			connection.execute(delete, (delete_value, ))
		connection.close()

