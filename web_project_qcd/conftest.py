# @Time : 2019/10/16 16:22 
# @Author : zhang_san_jin
# @File : conftest.py 
# @Software: PyCharm
# 使用pytest需要的代码
from selenium.webdriver import Chrome
import pytest

from web_project_qcd.pages.bid import BidPage
from web_project_qcd.pages.login import LoginPage
from web_project_qcd.pages.user import UserPage
from web_project_qcd.test_data.login_data import user_info_success


@pytest.fixture()
def init_web():
    """浏览器初始化工作"""
    driver = Chrome()
    login_page = LoginPage(driver)
    # 返回参数，继续执行下面代码
    yield driver, login_page
    # 关闭浏览器
    driver.quit()

@pytest.fixture()
def init_bid():
    """投资的初始化工作"""
    driver = Chrome()
    login_page = LoginPage(driver)
    login_page.login(user_info_success['username'], user_info_success['pwd'])
    bid_page = BidPage(driver)
    user_page = UserPage(driver)
    yield driver,login_page,bid_page,user_page
    driver.quit()
@pytest.fixture(scope='class',autouse=True)   #类级别
def class_fixture():
    print("class before")
    yield
    print("class after")

@pytest.fixture(scope='module',autouse=True)   #模块级别
def module_fixture():
    print("module before")
    yield
    print("module after")

@pytest.fixture(scope='session',autouse=True)   #会话级别  autouse=True自动发现
def session_fixture():
    print("session before")
    yield
    print("session after")
