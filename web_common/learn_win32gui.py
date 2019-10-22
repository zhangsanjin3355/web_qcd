# @Time : 2019/8/30 10:30 
# @Author : zhangsanjin
# @File : learn.py 
# @Software: PyCharm

import win32gui
import win32con
import time
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
driver = webdriver.Chrome()
# session_id=driver.session_id
# url = "https://localhost:9515/session/{}/url".format(session_id)
# baidu_url ='https://www.baidu.com'
# data = {"url":baidu_url}
# requests.post(url,json=data)
# driver.implicitly_wait(30)
# 发起get请求
url = "https://www.ketangpai.com/Home/User/login.html"
driver.get(url)
#窗口最大
driver.maximize_window()
#显示等待函数
def wait_find_element(located) -> WebElement:
    wait = WebDriverWait(driver, timeout=40,poll_frequency=0.5)
    ele = wait.until(ec.presence_of_element_located(located))
    return ele
#定位账号
zhang_hao = wait_find_element((By.XPATH,"//input[@name='account']"))
zhang_hao.send_keys('15311119695')
#定位密码
mi_ma = wait_find_element((By.XPATH,"//input[@name='pass']"))
mi_ma.send_keys('fq81574621')
#点击登陆，点击
deng_lu = wait_find_element((By.XPATH,"//div[@class='padding-cont pt-login']//a[text()='登录']"))
deng_lu.click()
#菜单界面关闭按钮，点击
guan_bi = wait_find_element((By.XPATH,"//a[@class='close']")).click()
#点击py14期
py14 = wait_find_element((By.XPATH,"//a[@title='py14期考核' and @class='jumptoclass']")).click()
#点击作业
zuo_ye = wait_find_element((By.XPATH,"//a[text()='作业']")).click()
#点击第一个上传作业
shangchuan_zuoye = wait_find_element((By.XPATH,"//a[text()='上传作业']")).click()
#点击添加作业
tianjia_zuoye=wait_find_element((By.XPATH,"//div[text()='添加作业文件']//following-sibling::div//label")).click()
#打开窗口后一定要设置强制等待，不然找不到也不会报错
time.sleep(4)
# #1、找到对应的窗口
dialog = win32gui.FindWindow("#32770",u"打开")  #一级
time.sleep(4)
# #2、找到下级窗口  参数1母体句柄  参数2母体后面第几个窗口0开始 参数3子窗口类名 参数4窗口名字None
ComboBoxEx32 = win32gui.FindWindowEx(dialog,0,"ComboBoxEx32",None)  #二级  上级参数
time.sleep(4)
comboBox = win32gui.FindWindowEx(ComboBoxEx32,0,"ComboBox",None)  #三级
time.sleep(4)
edit = win32gui.FindWindowEx(comboBox,0,"Edit",None)  #四级   输入框
time.sleep(4)
button = win32gui.FindWindowEx(comboBox,0,"Button",None)  #二级   按钮
time.sleep(4)
# #操作 参数1句柄 参数2要发送的消息  参数3消息的参数
win32gui.SendMessage(edit,win32con.WM_SETTEXT,None,r'C:\Users\lenovo\Desktop\联迪E350.txt')  # 发送文件路径 win32con.WM_SETTEXT重新设置的指令  D:\\apk.txt要发送的文件
time.sleep(4)
win32gui.SendMessage(dialog,win32con.WM_COMMAND,1,button)  #点击打开按钮
time.sleep(4)





