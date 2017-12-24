# encoding:utf-8
import threading
import time
import os
import pymysql.cursors


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
connection = pymysql.connect(host='localhost', user='root', password='123456',
                             db='students', port=3306, charset='UTF8')

# 2.定义一个游标
cur = connection.cursor()

# 3.sql语句构建
sql = r'select*from info where name!="mysql";'

# 4.执行sql语句
try:
    cur.execute(sql)
    result = cur.fetchall()
    for rows in result:
        name = rows[0]
        addr = rows[1]
        tel = rows[2]
        print('{}{}{}'.format(name, addr, tel))
except Exception as e:
    raise e
finally:
    connection.close()
