from baseView.base import BaseView
from selenium.webdriver.common.by import By
from frameword.common import Common
import time
from frameword.logger import Logger


logger=Logger(logger='H5').getlog()
class H5(BaseView):
    kaoyan_go_h5=(By.ID,'com.tal.kaoyan:id/mainactivity_button_find')
    h5_go_2019kaoyan=(By.XPATH,'/html/body/div[1]/div/div[1]/ul/li[1]/a')


    def goH5(self):
        self.click(*self.kaoyan_go_h5)
        time.sleep(3)
        logger.info('进入H5页面')
        # swip=Common(self.driver)
        # swip.get_screenSize()
        # swip.swipeUp()
        # time.sleep(3)
        # swip.swipeDown()
        # time.sleep(3)
        # swip.swipeLeft()
        # time.sleep(3)
        # swip.swipeRight()

        #
        '''切换contexts'''

        self.driver.switch_to.context('WEBVIEW_com.android.launcher')
        logger.info('切换context成功！')
        time.sleep(3)
        self.click(*self.h5_go_2019kaoyan)
        logger.info('点击H5页面成功！')
        time.sleep(3)
        self.driver.switch_to.context('NATIVE_APP')

