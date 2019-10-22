# @Time : 2019/10/12 16:56 
# @Author : zhangsanjin
# @File : bid.py 
# @Software: PyCharm
from selenium.webdriver.common.by import By

from web_project_qcd.pages.base import BasePage

class BidPage(BasePage):
    """投资页面 pageobject"""
    #投资输入框定位
    bid_input_locator = (By.XPATH,"//input[contains(@class ,'unit-investinput')]")
    #投资按钮的元素定位
    bid_submit_button = (By.XPATH,"//button[contains(@class,'btn-special')]")
    #投资激活定位
    alter_active_locator = (By.XPATH,"//div[@class='layui-layer-content']//button[text()='查看并激活']")

    def get_bid_input_element(self):
        """定位投资输入框"""
        return self.wait_find_element(self.bid_input_locator)
    def click_bid_submit(self):
        """点击投资按钮"""
        e = self.wait_clickable_element(self.bid_submit_button)
        e.click()
    def click_alter(self):
        """点击激活并查看"""
        e = self.wait_clickable_element(self.alter_active_locator)
        e.click()