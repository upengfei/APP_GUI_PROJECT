# -*- coding:utf-8 -*-
import MySQLdb
import sys
import conf_read
from func.logInfo import logger


class MysqlDB(object):
    """
    数据库操作
    """

    def __init__(self,path):

        self.rf = conf_read.ReadFile(path)
        try:
            self.conn = MySQLdb.connect(
                host=self.rf.get_option_value("db", "db_host"),
                user=self.rf.get_option_value("db", "db_user"),
                passwd=self.rf.get_option_value("db", "db_passwd"),
                db=self.rf.get_option_value("db", "db_name"),
                port=int(self.rf.get_option_value("db", "db_port")),
                charset="utf8"
            )
            self.cursor = self.conn.cursor()
        except Exception as e:
            print e



    def execute(self, sql, arg=None):
        """
        执行单条sql语句,接收的参数为sql语句本身和使用的参数列表,返回值为受影响的行数
        :param sql:
        :param arg:
        :return:
        """
        try:
            self.cursor.execute(sql, args=arg)
        except Exception as e:

            print e

    def executemany(self, sql, args):
        """
         执行单条sql语句,但是重复执行参数列表里的参数,返回值为受影响的行数
        """
        try:
            self.cursor.executemany(sql, args=args)
        except Exception as e:

            print e

    def fetchone(self):
        """
        返回一条结果行；
        执行完后指针发生移动，配合scroll方法来移动指针(同样适用于fetchall/fetchmany)
        """
        try:
            return self.cursor.fetchone()
        except Exception as e:

            print e

    def fetchall(self):
        ''' 接收全部的返回结果行 '''
        try:
            return self.cursor.fetchall()
        except Exception as e:
            print e

    def fetchmany(self, num):
        """
        接收num条返回结果行.如果num的值大于返回的结果行的数量,则会返回cursor.arraysize条数据
        :param num:
        :return:
        """
        try:
            return self.cursor.fetchmany(size=num)
        except Exception as e:
            print e


    def cursor_close(self):
        self.cursor.close()

    def conn_close(self):
        self.conn.close()

    def conn_commit(self):
        self.conn.commit()

    def scroll(self, value, mode='relative'):
        """
        移动指针到某一行.如果mode='relative',则表示从当前所在行移动value条,
        如果 mode='absolute',则表示从结果集的第一行移动value条.
        :param value:
        :param mode:
        :return:
        """
        self.cursor.scroll(value, mode=mode)

