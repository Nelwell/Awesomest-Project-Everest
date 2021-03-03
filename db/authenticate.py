import hashlib
import crypt


def hash_password(password, salt):
	salted_password = f'{salt}{password}'	# Add password and salt for added security
	byte_string = str.encode(salted_password)	# Convert to bytes to for hashing
	salty_hashbrowns = hashlib.sha512(byte_string)	# Hash bytes using SHA
	hashed_in_int = hash(salty_hashbrowns)	# Convert to int for easy comparison/storage

	return hashed_in_int


def create_salt():
	'''Couldn't remember how to make a salt in python, credit goes to lorenzi in this post:
	 https://stackoverflow.com/questions/5293959/creating-a-salt-in-python'''
	salt = crypt.mksalt(crypt.METHOD_SHA512)	# Create 16 char long salt
	return salt


def passwords_match(password, salt, valid_credentials):
	test_credentials = hash_password(password, salt)

	return test_credentials == valid_credentials:
