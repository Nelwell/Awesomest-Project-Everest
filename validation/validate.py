import re

def is_valid_email(email_string):
	email_vaild = re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",email_string)
	return email_vaild


def is_valid_password():
	pass


def is_valid_json():
	pass
