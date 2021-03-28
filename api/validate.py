import json

def is_valid_json(jsonData): 
	#https://pynative.com/python-json-validation/ Shamelessly copied. 
	#Returns a value error if the json is invalid and returns false, otherwise returns true.
    try:
        json.loads(jsonData)
        return True
    except ValueError as err:
        return False
