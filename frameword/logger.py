import logging
import os.path
import time

class Logger(object):
    def __init__(self,logger):

        '''新建logging对象：logger'''
        self.logger=logging.getLogger(logger)

        '''设置logger对象的级别'''
        self.logger.setLevel(logging.DEBUG)

        '''这里开始设置日志相关内容'''
        '''这里开始设置日志相关内容'''
        '''这里开始设置日志相关内容'''

        '''设置当前时间和路径，并：命名'''
        log_path=os.path.dirname(os.path.abspath('.'))+'/logs/'
        rq=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        log_name=log_path+rq+'.log'

        '''创建一个handler对象，并写入文件'''
        fh = logging.FileHandler(log_name,encoding='utf-8',mode="a+")  #对象的参数是：路径+时间+后缀 FileHandler是写入文件的Handler
        fh.setLevel(logging.INFO)   #设置级别

        '''再创建一个handler对象，输入到控制台'''
        ch = logging.StreamHandler()        #StreamHandler是输出到控制台的Handler
        ch.setLevel(logging.INFO)

        '''设置输出格式'''
        formatter=logging.Formatter('%(asctime)s- %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)  #设置文件格式
        ch.setFormatter(formatter)  #设置控制台格式

        '''这里开始设置日志相关内容结束'''
        '''这里开始设置日志相关内容结束'''
        '''这里开始设置日志相关内容结束'''

        '''将设置好格式的控制台对象和文件对象，被logger添加到handler'''
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    '''提供对外访问的公共方法'''
    def getlog(self):
        return self.logger

