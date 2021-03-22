import re
import json


def is_valid_email(email_string):
    email_valid = re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email_string)
    return email_valid


def is_valid_password(password):
    # at least 8 characters, must contain at least 1 uppercase letter, 1 lowercase letter, and 1 number, Can contain special characters - by psutton3756 - regexr.com/3bfsi
    password_valid = re.match("^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$", password)
    return password_valid


def is_valid_json(jsonData): 
	#https://pynative.com/python-json-validation/ Shamelessly copied. 
	#Returns a value error if the json is invalid and returns false, otherwise returns true.
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True
