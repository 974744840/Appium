import unittest
from test_case.base_test import BaseTestCase
from baseView.todolist_longView import Longin


'''
todolist 实现登录--添加待办事项
todolist 实现登录-删除
'''
class Function_1(BaseTestCase):
    def test_long_add_delete(self):
        login=Longin(self.driver)
        login.login_way('1','1')
        login.add_affair('哈哈哈')
        login.delete_affair()

if __name__ == '__main':
    unittest.main()

