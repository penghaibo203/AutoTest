import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome()
# browser = webdriver.Firefox()
browser.implicitly_wait(5)
name = browser.name
print(name)

url = "http://test1.zmninfo.com/SimulationElement/"
browser.get(url)
browser.maximize_window()

title = browser.title
print(title)
current_url = browser.current_url
print(current_url)
print(browser.page_source)

# time.sleep(10)

# browser.close()

# xpath

# 定位单个元素
# 单行文本框
# ID，优先通过来定位；其次可以用name来定位；考虑用XPATH来定位
# tag name、css选择器、class属性的方式来定位元素

ele_id = browser.find_element_by_id("t1")
ele_id.send_keys("abc")

ele_name = browser.find_element_by_name("t1")
ele_name.send_keys("efg")

ele_xpath = browser.find_element_by_xpath("//input[contains(@class, 'text')]")
ele_xpath.send_keys("123")

ele_class = browser.find_element_by_class_name("text")
ele_class.send_keys("class")

ele_tag = browser.find_element_by_tag_name("textarea")
ele_tag.send_keys("area is here")

ele_css = browser.find_element_by_css_selector(".text")
ele_css.send_keys("css")

# 针对超链接的定位及操作
ele_href = browser.find_element_by_link_text("新标签页打开Bing")
ele_href.click()

ele_href_p = browser.find_element_by_partial_link_text("打开Bing")
ele_href_p.click()

ele_href_x = browser.find_element_by_xpath("//a[contains(@href, 'https://www.bing.com/')]")
ele_href_x.click()

# 删除已输入的内容
ele_id.clear()

ele_class.send_keys(Keys.BACKSPACE)
ele_class.send_keys(Keys.BACKSPACE * 3)

# 光标的移动，连选
ele_class.send_keys(Keys.LEFT * 5, Keys.BACKSPACE)
ele_class.send_keys(Keys.SHIFT, Keys.RIGHT * 3)

# 另外一种找元素的方式,text()
ele_c2 = browser.find_element_by_xpath("//div[contains(text(),'请单击这里')]")
ele_c2.click()

# 双击
ele_dc = browser.find_element_by_xpath("//div[contains(@ondblclick,'myFc(this)')]")
ac = webdriver.ActionChains(browser)
ac.double_click(ele_dc)
ac.perform()

# 悬浮
ele_f = browser.find_element_by_xpath("//div[contains(text(),'把鼠标移到上面')]")
ac.move_to_element(ele_f).perform()

# 拖拽
ele_d1 = browser.find_element_by_xpath("//div[@data-dad-id='1']")
ele_d2 = browser.find_element_by_xpath("//div[@data-dad-id='2']")
webdriver.ActionChains(browser).drag_and_drop(ele_d1, ele_d2).perform()

for i in range(1,6):
    webdriver.ActionChains(browser).drag_and_drop(browser.find_element_by_xpath("//div[@data-dad-id='%s']" % i), browser.find_element_by_xpath("//div[@data-dad-id='6']")).perform()


ele_xuanfu = browser.find_element_by_link_text("链 接")
webdriver.ActionChains(browser).move_to_element(ele_xuanfu).perform()
ele_news = browser.find_element_by_link_text("新闻")
webdriver.ActionChains(browser).move_to_element(ele_news).perform()

ele_select = browser.find_element_by_id("s1Id")
sel = Select(ele_select)
sel.select_by_value("o2")
sel.select_by_visible_text("o03")

#警告框处理
ele_button = browser.find_element_by_name("b1")
ele_button.click()
ele_alert = browser.switch_to.alert
ele_alert.accept()
ele_alert.dismiss()
ele_alert.send_keys("hello!")

#WebElement
#页面滚动----通过执行js脚本来完成
js_1 = "window.scrollTo(0,0)"
browser.execute_script(js_1)
js_2 = "window.scrollTo(0,document.body.scrollHeight)"
browser.execute_script(js_2)

#页面滚动到指定的元素控制，防止页面元素被定位到之后没有自动滚动过去
js_ele = "arguments[0].scrollIntoView()"
browser.execute_script(js_ele, ele_button)
ele_button.click()

#打开新标签页
js_open = "window.open()"
browser.execute_script(js_open)
browser.switch_to.window

#time.sleep()强制等待
#time.sleep(5)
#显示等待，只需要被指定等待的元素到位了即可
#隐式等待，写法上一般在浏览器打开的时候就加上

#截屏
browser.save_screenshot("aaa.png")