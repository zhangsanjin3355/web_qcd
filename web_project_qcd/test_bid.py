# @Time : 2019/10/12 15:11 
# @Author : zhangsanjin
# @File : test_bid.py 
# @Software: PyCharm
"""投资前置条件：
1、登录
2、账户有无余额  无：充值
3、标的有没有钱
"""
import unittest

import pytest
from selenium import webdriver

from web_project_qcd.pages.bid import BidPage
from web_project_qcd.pages.index import IndexPage
from web_project_qcd.pages.login import LoginPage
from web_project_qcd.test_data.bid_data import invest_money
from web_project_qcd.test_data.login_data import user_info_success
from web_project_qcd.pages.user import UserPage

class TestBid():
    @pytest.mark.bid
    def test_bid_success(self,init_bid):
        """在首页选择标的,点击 choose_bid()"""
        self.driver,self.login_page,self.bid_page,self.user_page=init_bid
        IndexPage(self.driver).choose_bid()
        #定位投资输入框元素 get_bid_input_element()
        e = self.bid_page.get_bid_input_element()

        #可用余额
        expect = float(e.get_attribute('data-amount')) #get_attribute获取属性值
        #发送投资金额
        e.send_keys(invest_money)
        #点击投资 click_bid_submit()
        self.bid_page.click_bid_submit()
        #点击激活并查看
        self.bid_page.click_alter()
        #获取投资后的可用余额
        actual_money_str = self.user_page.get_user_money()  #字符串
        actual_money = float(actual_money_str)    #把金额转成float

        #调试
        print("投资前余额",int(expect*100))
        print("投资金额", invest_money*100)
        print("投资后余额", int(actual_money*100))
        #断言
        # self.assertTrue(int(expect*100)-invest_money*100 ==int(actual_money*100))
        assert (int(expect*100)-invest_money*100 ==int(actual_money*100))