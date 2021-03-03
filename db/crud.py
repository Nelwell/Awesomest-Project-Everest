def setup_database():
	#TODO create trip table
	create_sql = 'CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, name TEXT UNIQUE)'
	create_table(create_sql)
	create_sql = 'CREATE TABLE IF NOT EXISTS credentials (credential_id INTEGER PRIMARY KEY, name TEXT UNIQUE, email_address TEXT UNIQUE, password TEXT UNIQUE, salt TEXT UNIQUE, FOREIGN KEY(name) REFERENCES users(name))'
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
