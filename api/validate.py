from io import TextIOWrapper
import json

def is_valid_json(jsonData): 
	#Returns a value error if the json is invalid and returns false, otherwise returns true.
    try:
        if (type(jsonData) == dict):
            return True
        elif (type(jsonData) == str):
            json.loads(jsonData)
            return True
    except ValueError as err:
        return False

with open('tests/test.json') as test_json:
    test_data = json.load(test_json)
print(type(test_data))
print(is_valid_json(test_data))