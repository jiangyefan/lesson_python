#!/usr/bin/env python
#!coding=utf-8
#__author__:Administrator
#__date__:2017/7/11
import random
import time
from selenium import webdriver

print("123".center(20,'*'),"345".center(20,'*'))
print('{0:*^20},{1:*<20}'.format("123","345"))

print("%.2f"%123)
print(list(range(3)))

# counter=0
# while counter<3:
#     username=input("input your name:")
#     password=input("input your password:")
#     if username=="jiangjiang" and password=="jiangjiang":
#         print("welcome")
#         break
#     else:
#         print("invaild password or username")
#     counter+=1
# else:
#     print("nb")


a=['alex','blob','char','delta','alex']
print(a[1:3])
a.append('xuefeng')
a.insert(2,'jiangjiang')
print(a)
count_a=a.count('alex')
print(count_a)
print(a.index('alex'))

print('jiangjiang1' in a)
print(type(a) is list)

for i,v in enumerate(a):
    print(i,"=====",v)

abc=random.randint(100,200)
print(abc)