# @Time : 2019/10/14 15:53 
# @Author : zhangsanjin
# @File : user.py 
# @Software: PyCharm
from selenium.webdriver.common.by import By

from web_project_qcd.pages.base import BasePage


class UserPage(BasePage):
    """用户页面 pageobject"""
    user_money = (By.XPATH, "//li[@class='color_sub']")

    def get_user_money(self):
        """获取用户可用余额"""
        e = self.wait_find_element(self.user_money)
        money = e.text[:-1].strip()  # strip 去掉两边空格
        return money  # 字符串
