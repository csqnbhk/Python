# encoding:utf-8
import yagmail

yag = yagmail.SMTP(user='5201314@qq.com', password='xxxxxxxxxxx', host='smtp.qq.com')
send_contents = 'this is a test.l just use the yagmail lib to send a mail'
yag.send('5201315@qq.com', '良心库，yagmail', send_contents)

"""
password='xxxxxxxxxxx'中的xxxxxxxxxxx为QQ邮箱登录授权码。
不是明码。

"""










