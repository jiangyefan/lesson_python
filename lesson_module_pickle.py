#!/usr/bin/env python
#coding=utf-8
#__author__:Administrator
#__date__:2017/7/29

import pickle
#
def foo():
    print('ok')


# data=pickle.dumps(foo)
# with open('c:\\pickle.txt','wb') as f:
#     f.write(data)


#注意如果函数用pickle序列化后传递的话 对方也需要有这个函数，此例子就是需要在对方电脑闹上也需要用foo函数
with open('c:\\pickle.txt','rb') as f:
    data=pickle.load(f)

data()