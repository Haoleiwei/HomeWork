import re

s='我的电子邮件tom@gmail.com。将什么发送到jerry123@163.com或者3123432@qq.com.若遇特殊情况打电话给182123445678'

mail=list(re.findall(r'[a-zA-Z0-9]+@(?:[a-zA-Z0-9]+\.)+[a-zA-Z]+',s))

i=0

while i<len(mail):

    print('我的可用邮箱是:',mail[i])

    i=i+1

phonenumber=re.findall(r'1\d{11}',s)

print('电话号码：',phonenumber)
