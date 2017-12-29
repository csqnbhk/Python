# author:Demon
# time:2017/12/24
# function:learn regex
import re
import requests
from bs4 import BeautifulSoup
import json

# 1.要分析文本
# req = requests.get('https://tieba.baidu.com/index.html')
# text = req.text
#
# # 2.构建regex表达式(没有全部列出情况，要详细分析才可以。这里只是一个例子）
# regex_exception = r'src="(https.+?\.(jpg|jpeg))"'
#
# # 3.构建regex对象
# regex_object = re.compile(regex_exception)
#
# # 4.从指定文本获取要找的信息(存入list）
# html_list = re.findall(regex_object, text)
#
# # 5.查看信息
# for img_html in html_list:
#     print(img_html[0])
# print('总共有{}个URL'.format(html_list.__len__()

# 测试regex
text = """
 </div>
       <p class="pl">[法] 圣埃克苏佩里 / 马振聘 / 人民文学出版社 / 2003-8 / 22.00元</p>
      <div class="star clearfix">
    <span class="allstar45"></span>
     <span class="rating_nums">9.0</span>
    <span class="pl">(
                    231953人评价
    )</span>
    </div>
    
         <div class="star clearfix"><span class="allstar45"></span><span class="rating_nums">8.7</span>
                <span class="pl">
                    (
                            77082人评价
                    )
                </span></div>

"""

# 都用正则表达式
# regex = r'<span class="pl">\((.+?)\)</span>'
# regex_object = re.compile(regex, re.S)
# name_list = re.findall(regex_object, text)
# count = 0
# r1 = r'(\d.+?)\D'
# # re1_ob = re.compile(r1, re.S)
# for i in name_list:
#     print(i)


