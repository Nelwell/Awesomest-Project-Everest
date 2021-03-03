def setup_database():
	'''The three tables are users: storing base information about users; credentials: storing
	 information to authenticate within the application; and trips: storing api data about
	 trips user decides to bookmark.'''
	
	'''Username column is used for signing in, and providing foreign key to cred and trip
	 tables. Name column is used for printing meaningful messages to the user.'''
	create_sql = 'CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, username TEXT UNIQUE, name TEXT)'
	create_table(create_sql)
	'''Username acts as foreign key from users table; email address acts as alternate form of
	 authentication on sign in; password is stored as SHA-256 hashed value of password; salt is
	 stored to apply to password before hashing to entered password to verify stored encrypted
	 password and entered passwords match.'''
	create_sql = 'CREATE TABLE IF NOT EXISTS credentials (credential_id INTEGER PRIMARY KEY, username TEXT UNIQUE, email_address TEXT UNIQUE, password TEXT UNIQUE, salt TEXT UNIQUE, FOREIGN KEY(username) REFERENCES users(username))'
	create_table(create_sql)
	'''Username acts as a foreign key from users table; trip_start_time is time user called, or
	 planned from their ride; start/end lat/long columns are the location start and end points;
	 price is estimate gained from uber, or calculated value based on distance from transit;
	 is_transit is a boolean value determining if ride share or public transit.'''
	create_sql = 'CREATE TABLE IF NOT EXISTS trips (trip_id INTEGER PRIMARY KEY, username TEXT, trip_start_time DATETIME, trip_start_lat DECIMAL, trip_start_long DECIMAL, trip_stop_lat DECIMAL, trip_stop_long DECIMAL, price DECIMAL, is_transit BOOLEAN, FOREIGN KEY(username) REFERENCES users(username))'
	create_table(create_sql)

	'''Either this, or the previous create_sql strings and create_table calls should be commented
	 out, depending on whether or not lat/long is used, or if lat/long and address is needed,
	 based on whichever conversion is easier.'''

	'''Username acts as a foreign key from users table; trip_start_time is time user called, or
	 planned from their ride; start/end address columns are the location start and end points;
	 price is estimate gained from uber, or calculated value based on distance from transit;
	 is_transit is a boolean value determining if ride share or public transit.'''
	create_sql = 'CREATE TABLE IF NOT EXISTS trips (trip_id INTEGER PRIMARY KEY, username TEXT, trip_start_time DATETIME, trip_start_address TEXT, trip_start_city TEXT, trip_start_state TEXT, trip_stop_address TEXT, trip_stop_city TEXT, trip_stop_state TEXT, price DECIMAL, is_transit BOOLEAN, FOREIGN KEY(username) REFERENCES users(username))'
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
