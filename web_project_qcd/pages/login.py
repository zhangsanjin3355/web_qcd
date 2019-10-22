# @Time : 2019/10/10 15:19 
# @Author : zhangsanjin
# @File : login.py 
# @Software: PyCharm
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from web_project_qcd.pages.base import BasePage

class LoginPage(BasePage):
    '''登录页面 pageobject 类封装'''
    url = 'http://120.78.128.25:8765/Index/login.html'

    def login(self,username, pwd):
        '''输入用户名密码登录'''
        self.driver.get(LoginPage.url)
        # 输入登录名，密码
        user_ele = self.get_user_info()
        pwd_ele= self.get_pwd_info()
        user_ele.send_keys(username)
        pwd_ele.send_keys(pwd)
        # 提交
        user_ele.submit()
        return self.driver

    def get_flash_info(self):
        '''获取错误信息'''
        flash_ele = WebDriverWait(self.driver, timeout=20).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, '.form-error-info')))
        return flash_ele
    def get_alter_info(self):
        """获取弹幕错误信息"""
        alter_info = WebDriverWait(self.driver, timeout=20).until(
            ec.presence_of_element_located((By.XPATH,"//div[@class='layui-layer-content']")))
        return alter_info
    def clear_user_info(self):
        """清空用户信息"""
        self.clear_username() #清空用户名
        self.clear_pwd()  #清空密码

    def clear_username(self):
        """清空用户名"""
        return self.get_user_info().clear()

    def clear_pwd(self):
        """清空密码"""
        return self.get_pwd_info().clear()

    def get_user_info(self):
        #定位用户名元素
        user_ele = WebDriverWait(self.driver, timeout=20).until(
            ec.presence_of_element_located((By.NAME, 'phone')))
        return user_ele

    def get_pwd_info(self):
        #定位密码元素
        pwd_ele = WebDriverWait(self.driver, timeout=20).until(
            ec.presence_of_element_located((By.NAME, 'password')))
        return pwd_ele


    #1、增加可读性 2、代码可读  3、方便调用
    #控制函数颗粒度，方法不要太长，一屏