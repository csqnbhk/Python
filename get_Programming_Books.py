# author demon
# time:2017/12/31
# function:获取豆瓣的编程类书籍并存入数据库
import re
import requests
import pymysql
import random
import time

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


def parsehtml():

    # 总的信息list
    book_info = []
    # 书籍信息存放list
    name = []
    author = []
    press = []
    pub_year = []
    page = []
    price = []
    grade = []
    person = []

    # 每本书的URL
    book_url = []

    # 获取每本书籍的URL
    page = 0
    while page < 1:
        try:
            page_url = 'https://book.douban.com/tag/%E7%BC%96%E7%A8%8B?start='+str(page*20)+'&type=T'
            page += 1
            text = gethtml(page_url)
            re_book_url = r'<a class="nbg" href="(.+?)"'
            re_book_url = re.compile(re_book_url)
            allurl = re.findall(re_book_url, text)
            for url in allurl:
                book_url.append(url)
            print('获取第{}个页面成功,{}......'.format(page, page_url))
        except:
            print('获取第{}个页面失败，正在重新获取...'.format(page))
            page -= 1
            pass
        finally:
            pass


# 打印一下看看总的链接地址
#     for url in book_url:
#         print(url)
    print('总的页面数为:{}'.format(len(book_url)))
    print('bool_url如下:')
    print(book_url)
    # 获取每本书的详细信息
    url_id = 0
    time.sleep(3)
    while url_id < 1:
        try:
            time.sleep(1)
            url_id += 1
            # print(book_url[url_id-1])
            text = gethtml(book_url[url_id-1])
            # 1.获取书名
            regex = r'<span property="v:itemreviewed">(.+?)</span>'
            regex = re.compile(regex)
            name = re.findall(regex, text)
            name = name[0]

            # 2.获取作者
            # regex = r'<span class="pl">.+?作者.+?">(.+?)</a>'
            # regex = re.compile(regex, re.S)
            # author = re.findall(regex, text)
            # print(author)
            # author = author[0].replace("\n", "")
            # author = author.replace(' ', '')

            # 3.获取出版社
            regex = r'<span class="pl">出版社:</span> (.+?)<br/>'
            regex = re.compile(regex)
            press = re.findall(regex, text)
            press = press[0]
            # 4.获取出版日期
            regex = r'<span class="pl">出版年:</span> (.+?)<br/>'
            regex = re.compile(regex)
            pub_year = re.findall(regex, text)
            pub_year = pub_year[0]
            # 5.获取书籍页数
            regex = r'<span class="pl">页数:</span> (.+?)<br/>'
            regex = re.compile(regex)
            page = re.findall(regex, text)
            page = page[0]
            # 6.获取书籍定价
            regex = r' <span class="pl">定价:</span> (.+?)<br/>'
            regex = re.compile(regex)
            price = re.findall(regex, text)
            price = price[0]
            # 7.获取豆瓣评分
            regex = r'<strong class="ll rating_num " property="v:average"> (.+?) </strong>'
            regex = re.compile(regex)
            grade = re.findall(regex, text)
            grade = grade[0]
            # 8.获取评价人数
            regex = r'<a href="collections" class="rating_people"><span property="v:votes">(.+?)</span>人评价</a>'
            regex = re.compile(regex)
            person = re.findall(regex, text)
            person = person[0]
            # book_info.append([name, author, press, pub_year, page, price, grade, person])
            book_info.append([name, press, pub_year, page, price, grade, person])
            # print(book_info)
        except :
            url_id -= 1
            print('获取{}URL书籍失败，正在重新获取.....'.format(book_url[url_id]))
            pass
        finally:
            pass
    # 打印一下book_info一共有多少书籍
    print('book_info存放的书籍数目:{}'.format(len(book_info)))

    # 存入数据库
    print('开始写入数据库')
    cur.execute('set sql_safe_updates=0;')
    conn.commit()

    for i in book_info:
        sql = "insert into book(name,press,pub_year,page,price,grade,person) values('{}','{}','{}','{}','{}','{}','{}');".format(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
        # print(sql)
        cur.execute(sql)
        cur.execute('set sql_safe_updates=1')
    conn.commit()
    cur.close()
    print('插入数据了完成...')


if __name__ == '__main__':
    init()
    parsehtml()

