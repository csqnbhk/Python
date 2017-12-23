import httplib2
import urllib
import urllib.request
import webbrowser as web
import time
import os
import random

url = 'https://www.cnblogs.com/abc8023/p/4723691.html'
count = random.randint(1, 5)
print('count={}'.format(count))
j = 0
while j < count:
    i = 0
    while i < 5:
        web.open_new_tab(url)
        i = i + 1
        time.sleep(0.5)
    else:
        os.system('taskkill /F  /IM 360se.exe')
    print('killbrowser ', j, ' times')
    j = j + 1
print('done')