from selenium.webdriver.common.by import By
from baseView.base import BaseView
from frameword.logger import Logger

logger=Logger(logger='Longin').getlog()

class Longin(BaseView):
    todolist_user_input=(By.ID,'com.example.todolist:id/nameET')
    todolist_pwd_input=(By.ID,'com.example.todolist:id/passwordET')
    todolist_login_button_clike=(By.ID,'com.example.todolist:id/loginBtn')

    todolist_add_affair=(By.ID,'com.example.todolist:id/action_new')
    todolist_add_affair_content=(By.ID,'com.example.todolist:id/toDoItemDetailET')
    todolist_add_affair_button=(By.ID,'com.example.todolist:id/saveBtn')

    todolist_delete_affair=(By.XPATH,'//android.widget.ListView/android.widget.RelativeLayout[1]')
    todolist_delete_affair_button=(By.XPATH,'//android.widget.LinearLayout[2]/android.widget.RelativeLayout')
    todolist_sure_delete_affair_button=(By.ID,'android:id/button1')
    '''登陆'''
    def login_way(self,user,pwd):
        self.sendkeys(user,*self.todolist_user_input)
        self.sendkeys(pwd,*self.todolist_pwd_input)
        self.click(*self.todolist_login_button_clike)
        logger.info('登陆成功！！！')

    '''添加一个代办事务'''
    def add_affair(self,content):
        self.click(*self.todolist_add_affair)
        self.sendkeys(content,*self.todolist_add_affair_content)
        self.click(*self.todolist_add_affair_button)
        logger.info('添加一个代办事务成功！！！')

    '''删除一个待办事务'''
    def delete_affair(self):
        self.long_press(*self.todolist_delete_affair)
        self.click(*self.todolist_delete_affair_button)
        self.click(*self.todolist_sure_delete_affair_button)
        logger.info('删除一个代办事务成功！！！')


