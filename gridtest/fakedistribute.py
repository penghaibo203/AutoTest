from selenium import webdriver
import time
from selenium.webdriver import DesiredCapabilities
#HTMLUNIT 无头浏览器 headless browser
node_dict = {
    "http://127.0.0.1:5555/wd/hub":DesiredCapabilities.CHROME.copy(),
    "http://127.0.0.1:6666/wd/hub":DesiredCapabilities.HTMLUNIT.copy()
}

driver = {}

for k, v in node_dict.items():
    driver[k] = webdriver.Remote(command_executor=k, desired_capabilities=v)
    driver[k].implicitly_wait(10)
    driver[k].get("https://www.baidu.com/")

time.sleep(5)

for k in driver:
    driver[k].quit()