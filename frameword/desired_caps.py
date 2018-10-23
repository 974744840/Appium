import os.path
from configparser import ConfigParser
from appium import webdriver
from framework.logger import Logger


logger=Logger(logger='Desired_caps').getlog()

class Desired_caps(object):
    '''配置方法'''
    def appium_dedired(self):
        '''选择路径并读取ini文件里的内容'''
        config=ConfigParser()
        file_path=os.path.dirname(os.path.abspath('.'))+'/config/config.ini'
        config.read(file_path,encoding='utf-8')

        desired_caps={}
        '''配置机型及系统'''
        desired_caps['platformName']=config.get('phoneType','platformName')
        logger.info('你选择的系统是：       platformName：%s',desired_caps['platformName'])

        desired_caps['platformVersion']=config.get('phoneType', 'platformVersion')
        logger.info('你选择的系统版本是：     platformVersion：%s', desired_caps['platformVersion'])

        desired_caps['deviceName']=config.get('phoneType', 'deviceName')
        logger.info('你选择的设备名称是：     deviceName：%s', desired_caps['deviceName'])

        '''其他基本配置'''
        desired_caps['appPackage']=config.get('desiredCaps','appPackage')
        logger.info('你选择的app名是：     appPackage：%s', desired_caps['appPackage'])

        desired_caps['appActivity']=config.get('desiredCaps', 'appActivity')
        logger.info('启动该app：    appActivity')

        desired_caps['noReset']=config.get('desiredCaps', 'noReset')
        logger.info('是否重置app：   noReset：%s', desired_caps['noReset'])

        desired_caps['sessionOverride']=config.get('desiredCaps', 'sessionOverride')
        logger.info('是否每次新建session：  sessionOverride：%s', desired_caps['sessionOverride'])

        desired_caps['unicodeKeyboard']=config.get('desiredCaps', 'unicodeKeyboard')
        logger.info('键盘设置：  unicodeKeyboard：%s', desired_caps['unicodeKeyboard'])

        desired_caps['resetKeyboard']=config.get('desiredCaps', 'resetKeyboard')
        logger.info('键盘设置：  resetKeyboard：%s', desired_caps['resetKeyboard'])

        '''app路径'''
        desired_caps['appname'] = config.get('desiredCaps', 'appname')
        dir=os.path.dirname(os.path.abspath('.'))

        desired_caps['app']=dir+'/app/'+desired_caps['appname']
        logger.info('app路径：%s',desired_caps['app'])

        '''配置实体：driver'''
        desired_caps['ip'] = config.get('desiredCaps', 'ip')
        desired_caps['port'] = config.get('desiredCaps', 'port')
        self.driver=webdriver.Remote('http://'+str(desired_caps['ip'])+':'+str(desired_caps['port'])+'/wd/hub',desired_caps)
        logger.info('实例化driver成功!')

        self.driver.implicitly_wait(3)
        logger.info('隐式等待3秒！')

        return self.driver
    def tearDown(self):
        self.driver.quit()

# a=Desired_caps()
# a.appium_dedired()
