from baseView.base import BaseView
import os
import time
from selenium.webdriver.common.by import By
from framework.logger import Logger

logger=Logger(logger='Common').getlog()

class Common(BaseView):
    '''获取屏幕尺寸'''
    def get_screenSize(self):
        x = self.get_window_size()['width']
        y = self.get_window_size()['height']
        logger.info('成功获取屏幕尺寸，宽：%s，高：%s',x,y)
        return (x, y)

    '''左滑'''
    def swipeLeft(self):
        logger.info('左滑')
        l = self.get_screenSize()
        y1 = int(l[1] * 0.2)
        x1 = int(l[0] * 0.95)
        x2 = int(l[0] * 0.25)
        self.swipe(x1, y1, x2, y1, 1000)

    '''右滑'''
    def swipeRight(self):
        logger.info('右滑')
        l = self.get_screenSize()
        y1 = int(l[1] * 0.2)
        x1 = int(l[0] * 0.25)
        x2 = int(l[0] * 0.95)
        self.swipe(x1, y1, x2, y1, 1000)

    '''上滑'''
    def swipeUp(self):
        logger.info('上滑')
        l = self.get_screenSize()
        y1 = int(l[1] * 0.8)
        x1 = int(l[0] * 0.5)
        y2 = int(l[1] * 0.2)
        self.swipe(x1, y1, x1, y2, 1000)

    '''下滑'''
    def swipeDown(self):
        logger.info('下滑')
        l = self.get_screenSize()
        y1 = int(l[1] * 0.2)
        x1 = int(l[0] * 0.5)
        y2 = int(l[1] * 0.8)
        self.swipe(x1, y1, x1, y2, 1000)