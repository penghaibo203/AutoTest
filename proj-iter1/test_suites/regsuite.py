import unittest
from test_cases.register.reg4testv2 import ECRegister


def make_suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    suite.addTests(loader.loadTestsFromTestCase(ECRegister))
    # cases = [ECRegister("test_short_username"), ECRegister("test_reg_normal")]
    # suite.addTests(cases)

    return suite

