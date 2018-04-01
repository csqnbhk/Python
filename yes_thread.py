import requests
from bs4 import BeautifulSoup
import re
import time
import lxml
import json
import pymysql
import random
import numpy
import threading
import queue


queue = queue.Queue()
index = range(1, 103)
all_url = []


def gethtml(html):
    req = requests.get(html)
    if req.status_code == 200:
        req.encoding = 'GBK'
        return req.text
    else:
        print('get request failed')


def parsehtml(index_flag):
    url_origin = 'http://www.jokeji.cn'
    try:
        html = 'http://www.jokeji.cn/list29_' + str(index_flag) + '.htm'
        text = gethtml(html)

        # 构建正则获取第一个页面的所有 list_url
        regex_url = r'href="(.+?)"target="_blank"'
        regex_url_object = re.compile(regex_url)
        url_list = re.findall(regex_url_object, text)
        for item in url_list:
            url = url_origin + item
            all_url.append(url)
        print('爬取第{}个页面完成...'.format(index_flag))
    except:
        print('爬取第{}个页面异常,正在重新爬取....'.format(index_flag))
        pass
    finally:
        pass



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


class ThreadGetUrl(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            url_index = self.queue.get()
            parsehtml(url_index)
            self.queue.task_done()


if __name__ == '__main__':
    print('开始:')
    start_time = time.time()
    # 创建线程
    for i in range(200):
        t = ThreadGetUrl(queue)
        t.setDaemon(True)
        t.start()
    # 填充queue
    for i in index:
        queue.put(i)

    # 阻塞，等待线程结束
    queue.join()
    # 总的url
    for item in all_url:
        print(item)
    print('总共有:{}'.format(all_url.__len__()))
    print('所有页面如上...........')

    end_time = time.time()
    print('用时:{}'.format(end_time - start_time))
