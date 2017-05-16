# -*- coding:utf-8 -*-

import logging
from logging.handlers import RotatingFileHandler
import threading
import configparser
import os
from lib import read_conf,getLogDir

class LogSignleton(object):
    """
    log_level = '日志级别：CRITICAL = 50 ERROR = 40 WARNING = 30 INFO = 20 DEBUG = 10 NOTSET = 0'
    log_on = 'console_log_on  = 1 开启控制台日志，0则关闭，logfile_log_on = 1 开启文件日志， 0则关闭'
    """

    def __init__(self, file):
        config = read_conf(file)

        mutex=threading.Lock()
        mutex.acquire() # 上锁，防止多线程下出问题
        # rf = ReadFunc.ReadFile(path)
        self.log_filename =getLogDir()+os.sep+config.get('LOGGING', 'logFile')

        self.max_bytes_each = int(config.get('LOGGING', 'max_bytes_each'))
        self.backup_count = int(config.get('LOGGING', 'backup_count'))
        self.fmt = config.get('LOGGING', 'fmt')
        self.log_level_in_console = int(config.get('LOGGING', 'log_level_in_console'))
        self.log_level_in_logfile = int(config.get('LOGGING', 'log_level_in_logfile'))
        self.logger_name = config.get('LOGGING', 'logger_name')
        self.console_log_on = int(config.get('LOGGING', 'console_log_on'))
        self.logfile_log_on = int(config.get('LOGGING', 'logfile_log_on'))
        self.logger = logging.getLogger(self.logger_name)
        self.__config_logger()
        mutex.release()

    def get_logger(self):
        return self.logger

    def __config_logger(self):
        # 设置日志格式
        fmt = self.fmt.replace('|','%')
        formatter = logging.Formatter(fmt)

        if self.console_log_on == 1: # 如果开启控制台日志
            console = logging.StreamHandler()
            console.setFormatter(formatter)
            self.logger.addHandler(console)
            self.logger.setLevel(self.log_level_in_console)

        if self.logfile_log_on == 1: # 如果开启文件日志

            rt_file_handler = RotatingFileHandler(self.log_filename, maxBytes=self.max_bytes_each, backupCount=self.backup_count)
            rt_file_handler.setFormatter(formatter)
            self.logger.addHandler(rt_file_handler)
            self.logger.setLevel(self.log_level_in_logfile)

logsignleton = LogSignleton('logconfig.ini')
logger = logsignleton.get_logger()


if __name__=='__main__':
    logsignleton = LogSignleton('logconfig.ini')
    print logsignleton.log_filename