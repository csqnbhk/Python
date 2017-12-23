# encoding:utf-8
import yagmail

yag = yagmail.SMTP(user='374405702@qq.com', password='gaqpyccovwfqcabf', host='smtp.qq.com')
send_contents = 'this is a test.l just use the yagmail lib to send you a mail'
yag.send('1799803903@qq.com', '良心库，yagmail', send_contents)












