import re

def is_valid_email():
	pass


def is_valid_password(password):
	#at least 8 characters, must contain at least 1 uppercase letter, 1 lowercase letter, and 1 number, Can contain special characters - by psutton3756 - regexr.com/3bfsi
	password_valid = re.match("^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$", password)
	return password_valid


def is_valid_json():
	pass
