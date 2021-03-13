import hashlib
import bcrypt


def hash_password(password, salt):
	salted_password = f'{salt}{password}'  # Add password and salt for added security
	byte_string = salted_password.encode()  # Convert to bytes to for hashing
	salty_hashbrowns = hashlib.sha512(byte_string)  # Hash bytes using SHA
	digested_hashbrowns = salty_hashbrowns.hexdigest()  # Convert to hex str for easy comparison/storage

	return digested_hashbrowns


def create_salt():
	salt = bcrypt.gensalt()  # Create a hex string to be attached to user's password for added security

	return salt


def passwords_match(password, salt, valid_credentials):
	test_credentials = hash_password(password, salt)

	return test_credentials == valid_credentials
