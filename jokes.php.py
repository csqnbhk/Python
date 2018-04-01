# author:Demon
# time:2018/3/24
# function:获取一些笑话
import requests
from bs4 import BeautifulSoup
import re
import time
import lxml
import json
import pymysql
import random
headers = []


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
    req = requests.get(html)
    if req.status_code == 200:
        req.encoding = 'GBK'
        return req.text
    else:
        print('get request failed')


def parsehtml():

    joke_info = []
    style = []
    title = []
    content = []
    all_url = []
    page = 1
    # 都用正则表达式
    print('开始下载')
    # 102页
    url_origin = 'http://www.jokeji.cn'
    while page <= 1:
        try:
            html = 'http://www.jokeji.cn/list26_'+str(page)+'.htm'
            page = page + 1
            text = gethtml(html)

            # 构建正则获取第一个页面的所有 list_url
            regex_url = r'href="(.+?)"target="_blank"'
            regex_url_object = re.compile(regex_url)
            url_list = re.findall(regex_url_object, text)
            for item in url_list:
                url = url_origin+item
                all_url.append(url)
            print('爬取第{}个页面完成...'.format(page - 1))
        except:
            print('爬取第{}个页面异常,正在重新爬取....'.format(page))
            page = page - 1
            continue
            pass
        finally:
            pass


    # 总的url
    print('总共有:{}'.format(all_url.__len__()))
    for item in all_url:
        print(item)
    print('所有页面如上...........')

    for item in all_url:
        text = gethtml(item)
        # 获取笑话的内容
        regex_content = r'<span id="text110">(.+?)</span>'
        regex_content_object = re.compile(regex_content, re.S)
        content_list = re.findall(regex_content_object, text)
        for item in content_list:
            content.append(item)
    print('获取笑话有:{}'.format(content.__len__()))

    # 插入数据库
    conn = pymysql.connect(host='localhost', user='root', password='123456', db='stories', port=3306, charset='utf8')
    cur = conn.cursor()

    cur.execute('set sql_safe_updates=0;')
    conn.commit()  # 只有提交才可以，对下面生效
    cur.execute('start transaction')  # 事务处理
    print('正在写入数据库....')
    for item in content:
        sql = "insert into jokes(content) values('{}')".format(item)
        cur.execute(sql)
    cur.execute('set sql_safe_updates=1')
    conn.commit()
    conn.close()
    print('写入数据库完成!')


if __name__ == '__main__':
    init()
    parsehtml()
