import unittest
from frameword.desired_caps import Desired_caps
import time


class BaseTestCase(unittest.TestCase):

    def setUp(self):

        app_dirver=Desired_caps()
        self.driver=app_dirver.appium_dedired()
        time.sleep(10)



    def tearDown(self):
        self.driver.quit()