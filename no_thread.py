import requests
from bs4 import BeautifulSoup
import re
import time
import lxml
import json
import pymysql
import random


def gethtml(html):
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
    while page <= 102:
        try:
            html = 'http://www.jokeji.cn/list29_'+str(page)+'.htm'
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
    for item in all_url:
        print(item)
    print('总共有:{}'.format(all_url.__len__()))
    print('所有页面如上...........')

    """
    for item in all_url:
        text = gethtml(item)
        # 获取笑话的内容
        regex_content = r'<span id="text110">(.+?)</span>'
        regex_content_object = re.compile(regex_content, re.S)
        content_list = re.findall(regex_content_object, text)
        for item in content_list:
            content.append(item)
    print('获取笑话有:{}'.format(content.__len__()))
    """


if __name__ == '__main__':
    start_time = time.time()
    parsehtml()
    end_time = time.time()
    print('用时:{}'.format(end_time - start_time))
