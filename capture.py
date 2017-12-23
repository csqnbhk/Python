import requests
from bs4 import BeautifulSoup
import re
import time
import random
headers = []


def init():
    h1 = {'User-Agent': 'MMozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Chrome/55.0.2883.87 Safari/537.36'}
    h2 = {'User-Agent': 'MMozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0'}
    headers.append(h1)
    headers.append(h2)


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


if __name__ == '__main__':

    init()

    text = gethtml('https://tieba.baidu.com/f?kw=%B0%D9%B6%C8%CD%BC%C6%AC&fr=ala0&tpl=5')

    img_original_html = r'original="(.+?\.jpg)" '
    img_html = r'src="(https+.+?\.jpg)" '

    img_original_re = re.compile(img_original_html)
    img_re = re.compile(img_html)

    img_original_re_list = re.findall(img_original_re, text)
    img_re_list = re.findall(img_re, text)

    print('img_html_original总的图片链接数:{}'.format(img_original_re_list.__len__()))
    for i in img_original_re_list:
        print(i)

    print('img_html总的图片链接数:{}'.format(img_re_list.__len__()))
    for i in img_re_list:
        print(i)
    print('总的jpg图片数目:{}'.format(img_re_list.__len__()+img_original_re_list.__len__()))

    print('***********************正在下载图片************************')
    count = 1

    for img in img_original_re_list:
        req = requests.get(img, timeout=1)
        if req.status_code == 200:
            print('正在下载第{}张图片....'.format(count))
            filepath = 'C:\\Users\\Administrator\\Desktop\\capture\\' + str(count) + '.jpg'
            f = open(filepath, 'wb')
            f.write(req.content)
            f.close()
            print('第{}张图片下载完成。'.format(count))
            count = count+1
            if count % 20 == 0:
                time.sleep(1)

    for img in img_re_list:
        req = requests.get(img, timeout=1)
        if req.status_code == 200:
            print('正在下载第{}张图片....'.format(count))
            filepath = 'C:\\Users\\Administrator\\Desktop\\capture\\' + str(count) + '.jpg'
            f = open(filepath, 'wb')
            f.write(req.content)
            f.close()
            print('第{}张图片下载完成。'.format(count))
            count = count + 1
            if count % 20 == 0:
                time.sleep(1)

    print('******下载完成，总共下载了:{}张图片******'.format(count-1))
