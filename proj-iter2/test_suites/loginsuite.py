import unittest
from test_cases.login.login4test import LoginTest


def make_suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(LoginTest))

    return suite
