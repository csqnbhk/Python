# encoding:utf-8
import threading
import time
import os

number = 1
lock = threading.Lock()


def test():
    global number
    print('%s acquire Lock' % threading.current_thread().getName())
    if lock.acquire():
        print('%s get lock.' % threading.current_thread().getName())
        number=number+1
        print('%s leave lock.' % threading.current_thread().getName())
        lock.release()


if __name__ == '__main__':
    t1 = threading.Thread(target=test)
    t2 = threading.Thread(target=test)
    t3 = threading.Thread(target=test)
    t1.start()
    t2.start()
    t3.start()
    print('now the number={}'.format(number))
