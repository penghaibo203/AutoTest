from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import time

sele_grid_url = "http://127.0.0.1:4444/wd/hub"

capabilities = DesiredCapabilities.CHROME.copy()
capabilities["version"] = "7"
capabilities["platform"] = "WINDOWS"
driver = webdriver.Remote(sele_grid_url, desired_capabilities=capabilities)

driver.get("https://www.baidu.com/")
driver.implicitly_wait(7)
driver.maximize_window()
time.sleep(5)
driver.quit()



