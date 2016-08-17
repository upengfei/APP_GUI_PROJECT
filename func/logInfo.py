# -*- coding:utf-8 -*-

import logging
from logging.handlers import RotatingFileHandler
import threading
import configparser
import conf_read
import BasicFunc

class LogSignleton(object):
    """
    log_level = '日志级别：CRITICAL = 50 ERROR = 40 WARNING = 30 INFO = 20 DEBUG = 10 NOTSET = 0'
    log_on = 'console_log_on  = 1 开启控制台日志，0则关闭，logfile_log_on = 1 开启文件日志， 0则关闭'
    """
    def __init__(self, log_config):
        mutex=threading.Lock()
        mutex.acquire() # 上锁，防止多线程下出问题
        rf = conf_read.ReadFile(log_config)

        # config = configparser.ConfigParser()
        # config.read(log_config)

        self.log_filename = BasicFunc.Func().getLogDir() +'\\'+rf.get_option_value('LOGGING', 'log_file')
        self.max_bytes_each = int(rf.get_option_value('LOGGING', 'max_bytes_each'))
        self.backup_count = int(rf.get_option_value('LOGGING', 'backup_count'))
        self.fmt = rf.get_option_value('LOGGING', 'fmt')
        self.log_level_in_console = int(rf.get_option_value('LOGGING', 'log_level_in_console'))
        self.log_level_in_logfile = int(rf.get_option_value('LOGGING', 'log_level_in_logfile'))
        self.logger_name = rf.get_option_value('LOGGING', 'logger_name')
        self.console_log_on = int(rf.get_option_value('LOGGING', 'console_log_on'))
        self.logfile_log_on = int(rf.get_option_value('LOGGING', 'logfile_log_on'))
        self.logger = logging.getLogger(self.logger_name)
        self.__config_logger()
        mutex.release()



    def get_logger(self):
        return  self.logger

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

logsignleton = LogSignleton(r'\config\logconfig.ini')
logger = logsignleton.get_logger()