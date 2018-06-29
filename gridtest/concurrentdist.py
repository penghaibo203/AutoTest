import threading
from selenium import webdriver
import time
from selenium.webdriver import DesiredCapabilities

node_dict = {
    "http://192.168.2.60:5123/wd/hub":DesiredCapabilities.CHROME.copy(),
    "http://192.168.2.167:5688/wd/hub":DesiredCapabilities.CHROME.copy(),
    "http://192.168.2.112:6999/wd/hub":DesiredCapabilities.FIREFOX.copy(),
    "http://192.168.2.190:5521/wd/hub":DesiredCapabilities.CHROME.copy(),
    "http://192.168.2.128:6888/wd/hub":DesiredCapabilities.CHROME.copy(),
    "http://192.168.2.13:6446/wd/hub":DesiredCapabilities.CHROME.copy(),
}

driver = {}

def run_case(k, v):
    driver = webdriver.Remote(command_executor=k, desired_capabilities=v)
    driver.implicitly_wait(5)
    driver.get("https://www.baidu.com/")
    driver.maximize_window()
    driver.find_element_by_id("kw").send_keys("python多并发编程")
    driver.find_element_by_id("su").click()
    time.sleep(5)
    driver.quit()

def multi_run():
    threads = []
    for k, v in node_dict.items():
        threads.append(threading.Thread(target=run_case, args=(k, v)))

    for t in threads:
        t.start()

    for t in threads:
        t.join()


if __name__ == "__main__":
    multi_run()
    print("Done")

