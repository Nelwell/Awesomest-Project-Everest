import unittest
from validation.validate import *

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
