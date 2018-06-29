from biz.bizconfig import *
#POM实现版本
class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.url = ecshop_loginpage
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.username = self.driver.find_element_by_name("username")
        self.password = self.driver.find_element_by_name("password")
        self.remember = self.driver.find_element_by_id("remember")
        self.submit = self.driver.find_element_by_name("submit")

    def set_username(self, input_username):
        self.username.send_keys(input_username)

    def set_passwd(self, input_password):
        self.password.send_keys(input_password)

    def tick_remember(self):
        if not self.remember.is_selected():
            self.remember.click()

    def click_login_submit(self):
        self.submit.click()

    def login_to_echsop(self, input_username, input_password):
        self.set_username(input_username)
        self.set_passwd(input_password)
        self.tick_remember()
        self.click_login_submit()

