# encoding:utf-8
import threading
import time
import os
import pymysql.cursors
import requests
from bs4 import BeautifulSoup
import re
import  random

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

headers = []
conn = pymysql.connect(host='localhost', user='root', password='123456', db='book_db', port=3306, charset='utf8')
cur = conn.cursor()


def init():
    h1 = {'User-Agent': 'MMozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Chrome/55.0.2883.87 Safari/537.36'}
    h2 = {'User-Agent': 'MMozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0'}
    h3 = {'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; DigExt)'}
    headers.append(h1)
    headers.append(h2)
    headers.append(h3)


def gethtml(html):
    max_index = headers.__len__()-1
    index = random.randint(0, max_index)
    browser_header = headers[index]
    req = requests.get(html, headers=browser_header)
    if req.status_code == 200:
        req.encoding = 'utf-8'
        return req.text
    else:
        print('get request failed')


# 测试
if __name__ == '__main__':
    init()
    # text = gethtml('https://book.douban.com/subject/1148282/')
    text = 'https://book.douban.com/tag/%E7%BC%96%E7%A8%8B?start=0&type=T'
    regex = r'<div class="pub">(.+?)'
    regex = re.compile(regex, re.S)
    name = re.findall(regex, text)
    print(name)
    # regex = r'<span property="v:itemreviewed">(.+?)</span>'
    # regex = re.compile(regex)
    # name = re.findall(regex, text)
    # name = name[0]
    #
    # regex = r'<span class="pl">.+?作者.+?">(.+?)</a>'
    # regex = re.compile(regex, re.S)
    # author = re.findall(regex, text)
    # author = author[0].replace("\n", "")
    # author = author.replace(' ', '')
    #
    # regex = r'<span class="pl">出版社:</span> (.+?)<br/>'
    # regex = re.compile(regex)
    # press = re.findall(regex, text)
    # press = press[0]
    #
    # regex = r'<span class="pl">出版年:</span> (.+?)<br/>'
    # regex = re.compile(regex)
    # pub_year = re.findall(regex, text)
    # pub_year = pub_year[0]
    #
    # regex = r'<span class="pl">页数:</span> (.+?)<br/>'
    # regex = re.compile(regex)
    # page = re.findall(regex, text)
    # page = page[0]
    #
    # regex = r' <span class="pl">定价:</span> (.+?)<br/>'
    # regex = re.compile(regex)
    # price = re.findall(regex, text)
    # price = price[0]
    #
    # regex = r'<strong class="ll rating_num " property="v:average"> (.+?) </strong>'
    # regex = re.compile(regex)
    # grade = re.findall(regex, text)
    # grade = grade[0]
    #
    # regex = r'<a href="collections" class="rating_people"><span property="v:votes">(.+?)</span>人评价</a>'
    # regex = re.compile(regex)
    # person = re.findall(regex, text)
    # person = person[0]
    #
    # sql = "insert into book(name,author,press,pub_year,page,price,grade,person) values('{}','{}','{}','{}','{}','{}','{}','{}');".format(name, author, press, pub_year, page, price, grade, person)
    # print(sql)

    # print('开始写入数据库')
    # cur.execute('set sql_safe_updates=0;')
    # conn.commit()
    # cur.execute(sql)
    # cur.execute('set sql_safe_updates=1')
    # conn.commit()
    # cur.close()





