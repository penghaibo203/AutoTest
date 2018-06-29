from selenium import webdriver

driver = webdriver.Chrome()
#url = "https://www.baidu.com/"
url2= "http://test1.zmninfo.com/SimulationElement/"

driver.get(url2)
driver.maximize_window()

# ele_kw = driver.find_element_by_id("kw")
# ele_su = driver.find_element_by_id("su")
#
# ele_kw.send_keys("三只啄木鸟")
# ele_su.click()
#框架定位处理
# ele_iframe = driver.find_element_by_xpath("//iframe[@src='https://www.baidu.com']")
# driver.switch_to.frame(ele_iframe)
# ele_kw = driver.find_element_by_id("kw")
# ele_su = driver.find_element_by_id("su")
#
# ele_kw.send_keys("三只啄木鸟")
# ele_su.click()
#
# driver.switch_to.default_content()

for page in driver.window_handles:
    driver.switch_to.window(page)
    if driver.title in '微软 Bing 搜索 - 国内版':
        break;