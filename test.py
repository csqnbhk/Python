# encoding:utf-8
import threading
import time
import os
import pymysql.cursors
import requests
from bs4 import BeautifulSoup
import re

# 1.简单的测试thread

# number = 1
# lock = threading.Lock()
#
#
# def test():
#     global number
#     print('%s acquire Lock' % threading.current_thread().getName())
#     if lock.acquire():
#         print('%s get lock.' % threading.current_thread().getName())
#         number=number+1
#         print('%s leave lock.' % threading.current_thread().getName())
#         lock.release()
#
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=test)
#     t2 = threading.Thread(target=test)
#     t3 = threading.Thread(target=test)
#     t1.start()
#     t2.start()
#     t3.start()
#     print('now the number={}'.format(number))


# 1.测试连接mysql (在MySQL数据库中只能使用"utf8,UTF8",使用"uft-8,UTF-8"不行)
# connection = pymysql.connect(host='localhost', user='root', password='123456',
#                              db='books', port=3306, charset='UTF8')

# 2.定义一个游标
# cur = connection.cursor()

# 3.sql语句构建
# a = []
# a.append(['麦田的守望者', '9.0', '283344'])
# sql = r'select*from book_250;'
# # sql_set_charset = r'set names gbk;'
# # cur.execute(sql_set_charset)
# for item in a:
#     sqlqq = "insert into book_250(name,grade,person) values('{}','{}','{}');".format(item[0], item[1], item[2])
#     print(sqlqq)
#     cur.execute(sqlqq)
# cur.execute(sql)
# connection.commit()
# connection.close()
# 4.执行sql语句
# try:
#     cur.execute(sql)
#     result = cur.fetchall()
#     for rows in result:
#         name = rows[0]
#         addr = rows[1]
#         tel = rows[2]
#         print('{}{}{}'.format(name, addr, tel))
# except Exception as e:
#     raise e
# finally:
#     connection.close()


# 测试
# markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
# soup = BeautifulSoup(markup)
# a_tag = soup.a
# i_tag = soup.i.extract()
# print(a_tag)
# # <a href="http://example.com/">I linked to</a>
# print(i_tag)
# # <i>example.com</i>
#
# print(i_tag.parent)
# print('结束')












