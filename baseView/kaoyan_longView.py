from selenium.webdriver.common.by import By
from baseView.base import BaseView
from frameword.logger import Logger

logger=Logger(logger='Kaoyan_login').getlog()

class Kaoyan_login(BaseView):
    kaoyan_login_go_i_view=(By.ID,'com.tal.kaoyan:id/mainactivity_button_mysefl')
    kaoyan_login_dianji=(By.ID,'com.tal.kaoyan:id/activity_usercenter_logintip_img')
    kaoyan_login_user_input=(By.ID,'com.tal.kaoyan:id/login_email_edittext')
    kaoyan_login_pwd_input=(By.ID,'com.tal.kaoyan:id/login_password_edittext')
    kaoyan_login_button=(By.ID,'com.tal.kaoyan:id/login_login_btn')

    def kaoyan_login(self,user,pwd):
        self.click(*self.kaoyan_login_go_i_view)
        logger.info('进入我的个人界面。')
        self.click(*self.kaoyan_login_dianji)
        logger.info('点击登陆按钮。')
        self.sendkeys(user,*self.kaoyan_login_user_input)
        logger.info('输入账户成功！')
        self.sendkeys(pwd,*self.kaoyan_login_pwd_input)
        logger.info('输入密码成功！')
        self.click(*self.kaoyan_login_button)
        logger.info('点击登陆成功！')



