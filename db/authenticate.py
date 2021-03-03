import hashlib


def hash_password(password, salt):
	salted_password = f'{password}{salt}'	# Add password and salt for added security
	byte_string = str.encode(salted_password)	# Convert to bytes to for hashing
	salty_hashbrowns = hashlib.sha512(byte_string)	# Hash bytes using SHA
	hashed_in_int = hash(salty_hashbrowns)	# Convert to int for easy comparison/storage

	return hashed_in_int


def create_salt():
	pass


def passwords_match():
	pass
