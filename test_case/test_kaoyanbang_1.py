import unittest
from test_case.base_test import BaseTestCase
from baseView.kaoyan_longView import Kaoyan_login
from baseView.kaoyan_quitView import Quit
from baseView.kaoyan_H5 import H5
from frameword.common import Common
import time

class Start(BaseTestCase):
    def test_Start(self):
        # login=Kaoyan_login(self.driver)
        # login.kaoyan_login('www974744840','xiaoxinxin123')

        go_h5=H5(self.driver)
        go_h5.goH5()

        # quit=Quit(self.driver)
        # quit.quit()

if __name__ == '__main':
    unittest.main()