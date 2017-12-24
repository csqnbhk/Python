# author:Demon
# time:2017/12/24
# function:learn regex
import re
import requests

# 1.要分析文本
req = requests.get('https://tieba.baidu.com/index.html')
text = req.text

# 2.构建regex表达式(没有全部列出情况，要详细分析才可以。这里只是一个例子）
regex_exception = r'src="(https.+?\.(jpg|jpeg))"'

# 3.构建regex对象
regex_object = re.compile(regex_exception)

# 4.从指定文本获取要找的信息(存入list）
html_list = re.findall(regex_object, text)

# 5.查看信息
for img_html in html_list:
    print(img_html[0])
print('总共有{}个URL'.format(html_list.__len__()))
