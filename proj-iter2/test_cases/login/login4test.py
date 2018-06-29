from selenium import webdriver
import time
import ddt
import unittest
from pageobject.loginpage import LoginPage
from lib.myutility import get_testdata

@ddt.ddt
class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    @ddt.data(*get_testdata("./testdata/logininfo.txt"))
    @ddt.unpack
    def test_login_correct(self, value1, value2):
        obj = LoginPage(self.driver)
        obj.login_to_echsop(value1, value2)
        time.sleep(5)



