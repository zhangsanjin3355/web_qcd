# @Time : 2019/10/10 10:20 
# @Author : zhangsanjin
# @File : learn_pytest.py 
# @Software: PyCharm
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def login(username,pwd):
    '''输入用户名密码登录'''
    driver = webdriver.Chrome()
    driver.get('http://120.78.128.25:8765/Index/login.html')
    #等待函数
    # def wait_find_element(located):
    #     wait = WebDriverWait(driver,timeout=40)
    #     ele = wait.until(ec.presence_of_element_located(located))
    #     return ele
    user_ele = WebDriverWait(driver,timeout=20).until(
        ec.presence_of_element_located((By.NAME,'phone')))
    pwd_ele = WebDriverWait(driver,timeout=20).until(
        ec.presence_of_element_located((By.NAME,'password')))
    #输入登录d名，密码
    user_ele.send_keys(username)
    pwd_ele.send_keys(pwd)
    time.sleep(3)
    #提交
    user_ele.submit()
    return driver
class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass
    def test_login_success(self):
        driver = login('13760246701','python')
        user_ele = WebDriverWait(driver,timeout=20).until(
            ec.presence_of_element_located((By.XPATH,'/Member/index.html')))
        self.assertTrue('小蜜蜂96027837' in user_ele.text)
        time.sleep(2)