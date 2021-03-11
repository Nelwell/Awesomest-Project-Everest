import unittest
from validation.validate import *

class ValidatorTest(unittest.TestCase):

    def test_is_valid_email(self):
        test_email = "hi@hello.com"
        response = is_valid_email(test_email)
        self.assertTrue(response)