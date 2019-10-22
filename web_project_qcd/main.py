# @Time : 2019/10/16 14:40 
# @Author : zhang_san_jin
# @File : main.py 
# @Software: PyCharm
import pytest

if __name__ == '__main__':
    pytest.main(["-m demo",r"--html=report\test_1.html",r"--alluredir=report\allure"])
    #pytest.main(["-m bid", r"--html=report\test_2.html", r"--alluredir=report\allure"])