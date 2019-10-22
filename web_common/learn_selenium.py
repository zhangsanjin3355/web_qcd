# @Time : 2019/9/12 13:48 
# @Author : zhangsanjin
# @File : learn_selenium.py 
# @Software: PyCharm
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# 初始化的浏览器对象
driver = webdriver.Chrome()
# 隐式等待
driver.implicitly_wait(30)
# 发起get请求
url = "https://www.12306.cn/index/"
driver.get(url)
#窗口最大化
driver.maximize_window()
# 查找元素等待
def wait_find_element(located) -> WebElement:
    wait = WebDriverWait(driver, timeout=40,poll_frequency=0.5)
    ele = wait.until(ec.presence_of_element_located(located))
    return ele
# #点击按钮等待
# def wait_clickable_element(located) -> WebElement:
#     wait = WebDriverWait(driver, timeout=40, poll_frequency=0.5)
#     ele = wait.until(ec.element_to_be_clickable(located))
#     return ele
# js_code = "e = document.getElementById('train_date');"
# driver.execute_script(js_code)
# time.sleep(2)
# js_code1 = 'e.readOnly = false;'
# driver.execute_script(js_code1)# time.sleep(2)
# js_code2 = "e.value='2019-10-01'"
# driver.execute_script(js_code2)
# time.sleep(2)

data_ele = wait_find_element((By.ID,"train_date"))
js_code = 'arguments[0].readOnly=false'
driver.execute_script(js_code,data_ele)
js_code1= "arguments[0].value = '2019-10-07'"
driver.execute_script(js_code1,data_ele)
