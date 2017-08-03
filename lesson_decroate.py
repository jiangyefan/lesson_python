#!/usr/bin/env python
#coding=utf-8
#__author__:Administrator
#__date__:2017/7/22
import time

def outer():
    '''装饰器初识'''
    x=10
    def inner(): #inner是一个内部函数
        print(x)  #引用enlosing层的变量
    return inner #称innner函数就是一个闭包

#第一种调用方式
outer()()
#第二种调用方式
ret=outer()
ret() #闭包函数 inner

#注意，不能直接掉inner()因为是内部变量


#简单装饰器示例
#inner函数是一个闭包
#外层show_time包了一层做处理，返回内层inner函数内存地址，遵循开放封闭原则
#@show_time 装饰器的语法糖
#inner函数*args **kwargs的使用

def show_time(func):
    def inner(*args):
        start=time.time()
        func(*args)
        end=time.time()
        print('spend %s'%(end-start))
    return inner

#@show_time= foo=show_time(foo)
@show_time
def foo():
    print('foo')
    time.sleep(2)

#@show_time= bar=show_time(bar)

@show_time
def bar():
    print('bar')
    time.sleep(3)

@show_time
def add_diy(*args):
    sum=0
    for i in args:
        sum+=i
    print(sum)
    time.sleep(1)


# foo()
# bar()

# add_diy(3,4)




