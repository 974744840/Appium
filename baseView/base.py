from framework.logger import Logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os.path
from appium.webdriver.common.touch_action import TouchAction

logger=Logger(logger='BaseView').getlog()
class BaseView(object):
    def __init__(self,driver):
        self.driver=driver

    '''查找一个元素'''
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            logger.info('找到元素：%s',loc)
            return self.driver.find_element(*loc)
        except:
            self.get_windows_img()
            logger.error('%s页面中未找到%s元素' % (self,loc))

    '''查找一组元素'''
    def find_elements(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            logger.info('找到元素：%s',loc)
            return self.driver.find_elements(*loc)
        except:
            self.get_windows_img()
            logger.error('%s页面中未找到%s元素' % (self,loc))

    '''截图方法'''
    def get_windows_img(self):
        file_path=os.path.dirname(os.path.abspath('.'))+'/screenshots/'
        rq=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        screen_name=file_path+rq+'.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info('获取路径及文件名成功，如果报错将保存到：/screenshots/')
        except Exception as e:
            self.get_windows_img()
            logger.error('出现报错现象，已保存截图！%s',e)

    '''清除文本'''
    def clear(self, *loc):
        el = self.find_element(*loc)
        try:
            el.clear()
            logger.info('文本已经清除')
        except Exception as e:
            self.get_windows_img()
            logger.info('文本未清除，报错以截图：%s', e)

    '''输入的方法'''
    def sendkeys(self,text,*loc):
        el=self.find_element(*loc)
        el.clear()
        try:
            el.send_keys(text)
            logger.info('文本输入成功：%s',text)
        except Exception as e:
            self.get_windows_img()
            logger.error('文本输入失败：%s',e)

    '''点击元素'''
    def click(self, *loc):
        el = self.find_element(*loc)
        try:
            el.click()
            logger.info('点击完成。')
        except Exception as e:
            self.get_windows_img()
            logger.error('点击出错：%s', e)

    '''长按'''
    def long_press(self,*loc):
        el=self.find_element(*loc)
        try:
            action = TouchAction(self.driver)
            action.long_press(el).wait(20000).perform()
            logger.info('长按完成。')
        except Exception as e:
            self.get_windows_img()
            logger.error('长按出错：%s',e)

    '''获取屏幕大小'''
    def get_window_size(self):
        return self.driver.get_window_size()

    '''屏幕滑动'''
    def swipe(self,start_x, start_y, end_x, end_y, duration):
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def switch_to(self,context):
        self.driver.switch_to.context(context)
        logger.info('切换context成功！')

    def switch_to_app(self):
        time.sleep(3)
        self.driver.switch_to.context('NATIVE_APP')
        logger.info('切回app')