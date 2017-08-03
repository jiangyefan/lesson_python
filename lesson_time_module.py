#!/usr/bin/env python
#coding=utf-8
#__author__:Administrator
#__date__:2017/7/24

import time,datetime

#字符串格式

print(time.strftime('%F %T',time.localtime())) #struct_time转字符串
print(time.strftime('%F %T',time.gmtime()))  #UTC时间

print(time.asctime(time.localtime()))  #字符串另一种表现
print(time.asctime(time.gmtime()))  #struct_time转字符串

print(time.ctime(time.time()))  #时间戳转字符串

#时间戳格式 timestamp

print(time.time())

print(time.mktime(time.localtime()))
print(time.mktime(time.gmtime()))

#struct_time元组形式格式

print(time.strptime(time.asctime(time.localtime())))
print(time.strptime(time.ctime(time.time())))
print(time.strptime(time.asctime(time.localtime())))

print(time.ctime(time.mktime(time.localtime())))

print(datetime.datetime.now())


print(datetime.datetime.now()-datetime.timedelta(days=100))

 