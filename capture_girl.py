# author:Demon
# time:2017/12/27
# function:下载http://www.mzitu.com/网址的图片
import re
import os
import time
import random
import requests
from bs4 import BeautifulSoup

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
    req = requests.get(html, headers=browser_header)
    if req.status_code == 200:
        req.encoding = 'utf-8'
        return req.text
    else:
        print('get request failed')
        return None


if __name__ == '__main__':

    init()
    text = ''
    page_num = 0
    url_page = []
    origin_url = r'http://www.mzitu.com/113731/'

    re_html_down_url = r'src="(http.+?\.jpg)" '
    regex_url = re.compile(re_html_down_url)
    for i in range(1, 50):
        temp = origin_url+str(i)
        url_page.append(temp)
        print(temp)
        text = gethtml(temp)
        url_img = re.findall(regex_url, text)
        print(url_img)
        time.sleep(2)









