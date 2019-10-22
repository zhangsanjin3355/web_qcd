# @Time : 2019/10/11 14:53 
# @Author : zhangsanjin
# @File : index.py 
# @Software: PyCharm
import time
import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from web_project_qcd.pages.base import BasePage
from web_project_qcd.pages.login import LoginPage

class IndexPage(BasePage):
    """首页类 pageobject"""

    bid_locator = (By.XPATH,"//a[contains(@class,'btn-special')]")
    # def __init__(self,driver):
    #     self.driver = driver

    def get_user_info(self):
        '''获取首页的用户信息'''
        user_ele = self.wait_find_element((By.XPATH, "//a[@href='/Member/index.html']"))
        return user_ele

    def choose_bid(self):
        '''选择标的'''
        ele = self.wait_clickable_element(self.bid_locator)   #可点击时点击
        return ele.click()
