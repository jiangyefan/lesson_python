#!/usr/bin/env python
#coding=utf-8
#__author__:Administrator
#__date__:2017/7/24

import random
from functools import reduce

print(random.random())#随机打印0到1的数，不包括1

print(random.randint(1,10)) #参数是整形，随机返回在区间的数，包括10

print(random.randrange(1,100,2))#参数

print(random.choice([1,2,3]))#随机抽取一个序列中元素

print(random.sample([1,2,3],2))

a=[1,2,3]
random.shuffle(a)
print(a)

print(reduce(lambda x,y:x+y,range(1,6)))

print(list(map(lambda b,d:b+d,range(1,5),range(6,10))))

code=''
n=1
while n<7:
    ran_num=random.randint(1,10)
    ran_alp=chr(random.randint(65,91))
    add=random.choice([ran_num,ran_alp])
    n+=1
    code+=str(add)
print(code)


