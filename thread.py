"""
author:demon
time:2017/1/4
thread.py :测试简单线程创建，锁，线程安全queue

"""
# _*_coding:utf8_*_
import sys
import time
import queue
import threading
num = 10000
que = queue.deque()
mutex = threading.Lock()


def test1():
    global num
    global que
    while num > 0:
        mutex.acquire()
        que.append(num)
        num -= 1
        # time.sleep(1)
        mutex.release()
        print('线程1')


def test2():
    global num
    global que
    while num > 0:
        mutex.acquire()
        que.append(num)
        num -= 1
        # time.sleep(1)
        mutex.release()
        print('线程2')


def main():
    time_start = time.time()
    t1 = threading.Thread(target=test1, daemon=False)
    t2 = threading.Thread(target=test2, daemon=False)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('python中queue是线程安全的')
    time_end = time.time()
    print('运行时间:{}'.format(time_end-time_start))
    print(que)
    print('queue一共有:{}个元素'.format(que.__len__()))


if __name__ == '__main__':
    main()
