# @Time : 2019/10/15 10:15 
# @Author : zhang_san_jin
# @File : aaa.py 
# @Software: PyCharm
import time
import re
# a='aaaabbccdlksdjfkjabc'

# while a.find('ab')!=-1:
#
#     a= a.replace( 'ab','')
#     print(a)
# while a.find("ab")!=-1:
#     a = re.sub('ab','',a)
#     print(a)
import pytest


@pytest.fixture(scope='class')   #类级别
def class_print():
    print("class before")
    yield
    print("class after")

@pytest.fixture(scope='module')   #模块级别
def module_print():
    print("module before")
    yield
    print("module after")

@pytest.fixture(scope='session')   #会话级别
def session_print():
    print("session before")
    yield
    print("session after")

@pytest.fixture(scope="function")     #默认函数级别
def init_print():
    print("初始化浏览器")
    yield
    print("退出浏览器")

class Test_A:
    @pytest.mark.q
    def test_print_1(self,init_print,class_print,module_print,session_print):
        print("执行测试用例1")

    @pytest.mark.q
    def test_print_2(self,init_print, class_print, module_print,session_print):
        print("执行测试用例2")
class Test_B:
    @pytest.mark.q
    def test_print_3(self,init_print,class_print,module_print,session_print):
        print("执行测试用例3")