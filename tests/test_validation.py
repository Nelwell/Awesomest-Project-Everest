import unittest
import json
from validate import *
from api.validate import *

class ValidatorTest(unittest.TestCase):

    def test_is_valid_password(self):
        #contains a symbol
        test_password = "QuickBrownFox9$"
        response = is_valid_password(test_password)
        self.assertTrue(response)

        #no symbol
        test_password = "QuickBrownFox9"
        response = is_valid_password(test_password)
        self.assertTrue(response)

        #too few characters
        test_password = "Qu1ck"
        response = is_valid_password(test_password)
        self.assertFalse(response)

        #missing lowercase
        test_password = "QUICKBROWN!1"
        response = is_valid_password(test_password)
        self.assertFalse(response)

        #missing uppercase
        test_password = "quickbrown3"
        response = is_valid_password(test_password)
        self.assertFalse(response)

        #missing number
        test_password = "QuickbrownfoX"
        response = is_valid_password(test_password)
        self.assertFalse(response)

    def test_is_valid_email(self):
        # correct format should return true
        test_email = "hi@hello.com"
        response = is_valid_email(test_email)
        self.assertTrue(response)

        # bad format should return false
        test_email = "hi@hello"
        response = is_valid_email(test_email)
        self.assertFalse(response)

        # checking Top level domains with two letter separators
        test_email = "hi@hello.co.uk"
        response = is_valid_email(test_email)
        self.assertTrue(response)

        # checking spaces
        test_email = "hi @hello.co.uk"
        response = is_valid_email(test_email)
        self.assertFalse(response)

        # checking incorrect symbols
        test_email = "hi*@hello.co.uk"
        response = is_valid_email(test_email)
        self.assertFalse(response)
    
    def test_is_valid_json(self):
        #Check invalid json - https://pynative.com/python-json-validation/
        test_json = """{"name": "jane doe", "salary": 9000, "email": "jane.doe@pynative.com",}"""
        response = is_valid_json(test_json)
        self.assertFalse(response)

        #Check valid json - https://pynative.com/python-json-validation/
        test_json = """{"name": "jane doe", "salary": 9000, "email": "jane.doe@pynative.com"}"""
        response = is_valid_json(test_json)
        self.assertTrue(response)

        with open('tests/test.json') as test_json:
            test_data = json.load(test_json)
        response = is_valid_json(test_data)
        self.assertTrue(response)
