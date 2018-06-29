from selenium import webdriver
import time
import os

browser = webdriver.Chrome()
browser.implicitly_wait(5)

url = "http://127.0.0.1/ecshop/index.php"
browser.get(url)
browser.maximize_window()

ele_login = browser.find_element_by_partial_link_text("请登录")
ele_login.click()

ele_name = browser.find_element_by_name("username")
ele_name.send_keys("testifg")
ele_pwd  = browser.find_element_by_name("password")
ele_pwd.send_keys("123456")
ele_submit = browser.find_element_by_name("submit")
ele_submit.click()

time.sleep(10)

ele_uc = browser.find_element_by_partial_link_text("用户中心")
ele_uc.click()

ele_message = browser.find_element_by_partial_link_text("我的留言")
ele_message.click()

ele_img = browser.find_element_by_name("message_img")
ele_img.click()
os.startfile("C:\\Users\\Administrator\\Desktop\\upload.exe")
