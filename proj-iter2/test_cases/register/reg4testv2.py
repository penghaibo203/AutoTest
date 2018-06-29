import time
import ddt
import unittest
from selenium import webdriver
from biz import bizconfig
from lib.myutility import get_testdata


@ddt.ddt
class ECRegister(unittest.TestCase):
    def setUp(self):
        # 环境初始化的操作
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)
        self.browser.get(bizconfig.ecshop_homepage)
        self.browser.maximize_window()

    def tearDown(self):
        # 环境清理的相关操作
        if self.browser:
            self.browser.quit()

    @ddt.data(*get_testdata("./testdata/reginfo.txt"))
    @ddt.unpack
    def test_reg_normal(self, name, email, pwd, phone):
        username = name
        email = email
        passwd = pwd
        phone = phone

        # 跳转到注册页面
        browser = self.browser
        ele_link = self.browser.find_element_by_link_text("免费注册")
        ele_link.click()
        # 输入注册信息
        ele_username = browser.find_element_by_name("username")
        ele_username.send_keys(username)
        ele_email = browser.find_element_by_name("email")
        ele_email.send_keys(email)
        ele_pwd = browser.find_element_by_name("password")
        ele_pwd.send_keys(passwd)
        ele_pwd2 = browser.find_element_by_name("confirm_password")
        ele_pwd2.send_keys(passwd)
        ele_phone = browser.find_element_by_name("extend_field5")
        ele_phone.send_keys(phone)

        ele_agreement = browser.find_element_by_name("agreement")
        if not ele_agreement.is_selected():
            ele_agreement.click()

        # 提交注册请求
        ele_submit = browser.find_element_by_name("Submit")
        ele_submit.click()

        # 验证注册操作结果
        time.sleep(7)
        ele_welcome = browser.find_element_by_xpath("//b[@class='f4']")
        self.assertIn(username, ele_welcome.text, "获得注册成功的页面信息")

    @ddt.data("ss", "x", "")
    def test_short_username(self, name):
        username = name
        browser = self.browser
        browser.get(bizconfig.ecshop_regpage)

        ele_username = browser.find_element_by_name("username")
        ele_username.send_keys(username)
        ele_submit = browser.find_element_by_name("Submit")
        ele_submit.click()
        self.assertEqual("- 用户名长度不能少于 3 个字符。", browser.find_element_by_id("username_notice").text)


    def test_long_username(self):
        pass


if __name__ == "__main__":
    get_testdata("./testdata/reginfo.txt")
