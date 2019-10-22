# @Time : 2019/10/10 15:22 
# @Author : zhangsanjin
# @File : test_login.py 
# @Software: PyCharm
import time
# import unittest

import pytest
from selenium.webdriver import Chrome
from web_project_qcd.pages.index import IndexPage
from web_project_qcd.pages.login import LoginPage
from web_project_qcd.test_data.login_data import *


@pytest.mark.usefixtures("class_fixture")
class TestLogin():
    def test_login_success(self, init_web):
        '''登录(成功) login'''
        self.driver, self.login_page = init_web
        self.login_page.login("13760246701", "python")
        # 获取用户信息 get_user_info()
        user_ele = IndexPage(self.driver).get_user_info()
        assert ('小蜜蜂96027837' in user_ele.text)

    @pytest.mark.demo  # 打标记
    # @pytest.mark.skip("不想测试")  #skip跳过
    @pytest.mark.parametrize("data", user_info_error)  # 参数化，同DDT一样，data传递参数的参数名
    def test_login_1_error(self, data, init_web):  # 执行环境init_web   data,接收参数化的参数名
        """异常登录"""
        # 获取到初始化浏览器参数
        self.driver, self.login_page = init_web  # 接收init_web放回的driver,login_page的参数
        self.login_page.login(data['username'], data['pwd'])
        # 获取用户信息 get_flash_info()
        flash_ele = self.login_page.get_flash_info()
        # self.assertTrue(data['expected'] == flash_ele.text)
        assert (data['expected'] == flash_ele.text)
        self.driver.quit()

    @pytest.mark.unauth
    @pytest.mark.parametrize("data", user_info_authorize)
    def test_login_2_unauth(self, data, init_web):
        """异常登录_弹幕"""
        self.driver, self.login_page = init_web
        self.login_page.login(data['username'], data['pwd'])
        alter_info = self.login_page.get_alter_info()
        # self.assertTrue(data['expected'] == alter_info.text)
        assert (data['expected'] == alter_info.text)
