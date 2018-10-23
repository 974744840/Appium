import HTMLTestRunner
import os
import time
import unittest


'''执行当前文件夹左右以test开头的py文件
TestLoader：功能是批量运行的类
discover：功能是执行当前所有符合目录的文件
'''
test_dri='./'
suite=unittest.TestLoader().discover(test_dri,pattern='test*.py')

'''生成HTML报告文件'''
report_path = os.path.dirname(os.path.abspath('.'))+'/report/'
now = time.strftime('%Y-%m-%d-%H_%M_%S',time.localtime(time.time()))
HtmlFile = report_path+now+'_result.html'
fp = open(HtmlFile,'wb')

'''所有测试用例运行'''
if __name__=='__main__':
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"自动化测试报告，测试如下",description=u"用例测试情况如下")
    runner.run(suite)
    fp.close()