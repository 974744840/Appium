from selenium.webdriver.common.by import By
from baseView.base import BaseView
from frameword.logger import Logger

logger=Logger(logger='Quit').getlog()

class Quit(BaseView):
    user_quit_button=(By.ID,'com.tal.kaoyan:id/myapptitle_RightButton_textview')
    user_quit_suer_button_1=(By.ID,'com.tal.kaoyan:id/setting_logout_text')
    user_quit_suer_button_2=(By.ID,'com.tal.kaoyan:id/tip_commit')
    def quit(self):
        self.click(*self.user_quit_button)
        logger.info('进入设置页面。')
        self.click(*self.user_quit_suer_button_1)
        logger.info('点击退出按钮。')
        self.click(*self.user_quit_suer_button_2)
        logger.info('点击确认退出按钮。')
