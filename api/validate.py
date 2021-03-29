# This duplicates the validation module in the root directory. 
# All references to this should be switched to the root version.


from io import TextIOWrapper
import json

def is_valid_json(jsonData): 
	#   Returns a value error if the json is invalid and returns false, otherwise returns true.
    try:
        if (type(jsonData) == dict):
            return True
        elif (type(jsonData) == str):
            json.loads(jsonData)
            return True
    except ValueError as err:
        return False