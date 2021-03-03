def setup_database():
	create_sql = 'CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, username TEXT UNIQUE, name TEXT)'
	create_table(create_sql)
	create_sql = 'CREATE TABLE IF NOT EXISTS credentials (credential_id INTEGER PRIMARY KEY, username TEXT UNIQUE, email_address TEXT UNIQUE, password TEXT UNIQUE, salt TEXT UNIQUE, FOREIGN KEY(username) REFERENCES users(username))'
	create_table(create_sql)
	create_sql = 'CREATE TABLE IF NOT EXISTS trips (trip_id INTEGER PRIMARY KEY, username TEXT, trip_start_time DATETIME, trip_start_lat DECIMAL, trip_start_long DECIMAL, trip_stop_lat DECIMAL, trip_stop_long DECIMAL, price DECIMAL, FOREIGN KEY(username) REFERENCES users(username))'
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
