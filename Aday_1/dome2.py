import os
import unittest
import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

'''
todolist 实现登录--添加待办事项
todolist 实现登录-删除
'''
apk_path=os.path.dirname(os.path.abspath('.'))

class DomeTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = '127.0.0.1:21503'
        desired_caps['sessionOverride'] = True
        desired_caps['noReset'] = True
        desired_caps['app'] = apk_path + '/app/todolist.apk'
        desired_caps['appPackage'] = 'com.example.todolist'
        desired_caps['appActivity'] = 'com.example.todolist.LoginActivity'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()


