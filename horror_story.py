# author:Demon
# time:2018/3/16
# function:获取恐怖推理小故事100个
import requests
from bs4 import BeautifulSoup
import re
import time
import lxml
import json
import pymysql
import random
headers = []
conn = pymysql.connect(host='localhost', user='root', password='123456', db='stories', port=3306, charset='utf8')
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

    horror_story_info = []
    content = []
    answer = []
    content = ""
    answer = ""
    # 都用正则表达式
    print('开始下载')
    try:
        html = 'http://www.douban.com/note/565524701/?type=rec'
        text = gethtml(html)
        print('获取网页内容如下:')
        #print(text)
        # 1.获取内容

        regex_content = r'答案： <br>(.+?)<br><br><br></div>'
        regex_content_object = re.compile(regex_content, re.S)
        content_list = re.findall(regex_content_object, text)

        content = content_list[0].replace('<br>', '')
        content_list = []
        print(content)

        regex_content = r'\d+[、,](.+?)\d+[、,]'
        regex_content_object = re.compile(regex_content)
        ontent_list = re.findall(regex_content_object, content)
        print('content_list如下：')
        for item in content_list:
            print(item)
        #for item in content_list:
        #    content.append(item)
        """
        # 2.获取答案
        regex_answer = r''
        regex_answer_object = re.compile(regex_answer)
        answer_list = re.findall(regex_answer_object)
        for item in answer_list:
            answer.append(item)
            # time.sleep(10)
        """
    except :
        print('爬取页面异常.')
        pass

    """
    # 4.保存在文件中
    print('正在保存到文件中.....')
    f = open('horror_story_info.csv', 'w')
    f.write('故事，答案\n')
    for  item in horror_story_info:
        f.write(','.join(item) + '\n')
    f.close()
    print('写入文件完成.....')
    # 5.保存在数据库
    print('开始写入数据库')
    cur.execute('set sql_safe_updates=0;')
    conn.commit()   # 只有提交才可以，对下面生效
    cur.excute('start transaction;')    # 事务处理
    for item in horror_story_info:
        sql = "insert into book_250(name,grade,person) values('{}','{}','{}');".format(item[0], item[1], item[2])
        cur.execute(sql)
    cur.execute('set sql_safe_updates=1') 
    conn.commit()
    conn.close()
    print('写入数据库完成')
    """


if __name__ == '__main__':
    init()
    parsehtml()
