# author:Demon
# time:2017/12/29(也没有使用什么代理。还不会。代码写点有点乱)
# function:获取豆瓣排名250
import requests
from bs4 import BeautifulSoup
import re
import time
import lxml
import json
import pymysql
import random
headers = []
conn = pymysql.connect(host='localhost', user='root', password='123456', db='books', port=3306, charset='utf8')
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


def parsehtml():

    book_info = []
    name = []
    grade = []
    person = []
    page = 0
    # 都用正则表达式
    print('开始下载')
    while page < 10:
        try:
            html = 'https://book.douban.com/top250?start='+str(page*25)
            page = page + 1
            text = gethtml(html)
            # 1.获取书名
            regex_name = r'&#34; title="(.+?)"'
            regex_name_object = re.compile(regex_name)
            name_list = re.findall(regex_name_object, text)
            for item in name_list:
                name.append(item)
            # print(name)
            # 2.获取书的评分
            regex_grade = r'"rating_nums">(.+?)</span>'
            regex_grade_object = re.compile(regex_grade)
            grade_list = re.findall(regex_grade_object, text)
            for item in grade_list:
                grade.append(item)
            # print(grade)
            # # 3.获取评价人数
            regex_person = r'<span class="pl">\((.+?)\)</span>'  # 注意转义字符
            regex_person_object = re.compile(regex_person, re.S)
            person_list = re.findall(regex_person_object, text)
            regex_num = r'(\d.+?)\D'
            regex_num_object = re.compile(regex_num, re.S)
            for item in person_list:
                temp = re.findall(regex_num_object, item)
                person.append(temp)
            # print(person)

            # time.sleep(10)
        except :
            print('爬取第{}个页面异常,正在重新爬取....'.format(page))
            page = page - 1
            continue
            pass
        finally:
            pass
        print('爬取第{}个页面完成...'.format(page + 1))
    for item in range(name.__len__()):
        book_info.append([name[item], grade[item], person[item][0]])
    print('book_info:')
    print(book_info)
    # 4.保存在文件中
    print('正在保存到文件中.....')
    f = open('book250.csv', 'w')
    f.write('书名,评分,评价人数\n')
    for item in book_info:
        f.write(','.join(item) + '\n')
    f.close()
    print('写入文件完成.....')
    # 5.保存在数据库
    print('开始写入数据库')
    cur.execute('set sql_safe_updates=0;')
    conn.commit()   # 只有提交才可以，对下面生效
    for item in book_info:
        sql = "insert into book_250(name,grade,person) values('{}','{}','{}');".format(item[0], item[1], item[2])
        cur.execute(sql)
    conn.commit()
    cur.execute('set sql_safe_updates=1')
    conn.close()
    print('写入数据库完成')

if __name__ == '__main__':
    init()
    parsehtml()
