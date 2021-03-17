import unittest
from validation.validate import *

class ValidatorTest(unittest.TestCase):

    def test_is_valid_email(self):

        #correct format should return true
        test_email = "hi@hello.com" 
        response = is_valid_email(test_email)
        self.assertTrue(response)

        #bad format should return false
        test_email = "hi@hello"
        response = is_valid_email(test_email)
        self.assertFalse(response)
        
        #checking Top level domains with two letter separators
        test_email = "hi@hello.co.uk"
        response = is_valid_email(test_email)
        self.assertTrue(response) 

        #checking spaces
        test_email = "hi @hello.co.uk"
        response = is_valid_email(test_email)
        self.assertFalse(response) 

        #checking incorrect symbols
        test_email = "hi*@hello.co.uk"
        response = is_valid_email(test_email)
        self.assertFalse(response)
    