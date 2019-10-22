# @Time : 2019/10/12 15:52 
# @Author : zhangsanjin
# @File : base.py 
# @Software: PyCharm

#基类
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import logging

class BasePage:
    def __init__(self,driver):
        """初始化浏览器"""
        self.driver = driver

    def wait_find_element(self,located):
        '''等待元素出现'''
        try:
            ele = WebDriverWait(self.driver, timeout=20).until(
                ec.presence_of_element_located(located)
            )
            return ele
        except Exception as e:
            #1、打印log 2、截屏
            logging.error("不好啦，元素定位失败~ ~ ~")
            self.driver.save_screenshot('test.png')



    def wait_clickable_element(self, located):
        """等待元素可点击"""
        ele = WebDriverWait(self.driver, timeout=20).until(
            ec.element_to_be_clickable(located)
        )
        return ele
    def switch_iframe(self):
        """iframe切换"""
        pass
