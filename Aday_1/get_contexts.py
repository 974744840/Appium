from appium import webdriver
import os.path
import time


apk_path=os.path.dirname(os.path.abspath('.'))

desired_caps={}
'''这里在打开appium Service 的时候可以看到'''
desired_caps['platformName']='Android'      #被测设备系统
desired_caps['platformVersion']='6.0.1'     #被测系统版本

'''利用adb命令获取：adb devices'''
desired_caps['deviceName']='127.0.0.1:21503'    #被测系统的名称

desired_caps['sessionOverride']=True    #每次执行覆盖session
desired_caps['noReset']=True    #判断是否安装
desired_caps['app']=apk_path+'/app/kaoyanbang.apk'    #Android安卓包位置

'''
需用用adb中的：aapt d badging todolist.apk 命令  最后一个参数是路径下安装包
如果设置的是app包的路径：则不需要配置appPackage和appActivity 
'''
desired_caps['appPackage']='com.tal.kaoyan'   #APP包的名
desired_caps['appActivity']='com.tal.kaoyan.ui.activity.SplashActivity'    #启动的activity

driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)    #这里是给服务器发送基础配置信息
time.sleep(5)
driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_find').click()
contexts = driver.contexts
print(contexts)


driver.switch_to.context('WEBVIEW_com.android.launcher')
print('切换context成功！')
time.sleep(3)
driver.find_element_by_css_selector('body > div.header > div > div.main_nav.fl > ul > li:nth-child(3)').click()
print('点击H5页面成功！')
time.sleep(3)
driver.switch_to.context('NATIVE_APP')