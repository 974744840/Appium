from appium import webdriver
import os.path
'''包含操作：按压、长按、点击、移动、暂停'''
from appium.webdriver.common.touch_action import TouchAction
'''是多点触控类，可以模拟用户多点操作，有两个方法：add() 和 perform()'''
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.support.ui import WebDriverWait


'''获取当前根目录'''
apk_path=os.path.dirname(os.path.abspath('.'))

desired_caps={}
'''这里在打开appium Service 的时候可以看到'''
desired_caps['platformName']='Android'      #被测设备系统
desired_caps['platformVersion']='6.0.1'     #被测系统版本

'''利用adb命令获取：adb devices'''
desired_caps['deviceName']='127.0.0.1:21503'    #被测系统的名称

desired_caps['sessionOverride']=True    #每次执行覆盖session
desired_caps['noReset']=True    #判断是否安装
desired_caps['app']=apk_path+'/app/todolist.apk'    #Android安卓包位置

'''
需用用adb中的：aapt d badging todolist.apk 命令  最后一个参数是路径下安装包
如果设置的是app包的路径：则不需要配置appPackage和appActivity 
'''
desired_caps['appPackage']='com.example.todolist'   #APP包的名
desired_caps['appActivity']='com.example.todolist.LoginActivity'    #启动的activity

driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)    #这里是给服务器发送基础配置信息

driver.find_element_by_id('com.example.todolist:id/nameET').send_keys("1")
driver.find_element_by_id('com.example.todolist:id/passwordET').send_keys('1')
driver.find_element_by_id('com.example.todolist:id/loginBtn').click()

driver.find_element_by_id('com.example.todolist:id/action_new').click()
driver.find_element_by_id('com.example.todolist:id/toDoItemDetailET').send_keys('lalalalala')

driver.find_element_by_id('com.example.todolist:id/saveBtn').click()

action = TouchAction(driver)
delete=driver.find_element_by_xpath('//android.widget.ListView/android.widget.RelativeLayout[1]')
action.long_press(delete).wait(20000).perform()
driver.find_element_by_xpath('//android.widget.LinearLayout[2]/android.widget.RelativeLayout').click()
driver.find_element_by_id('android:id/button1').click()
