#!/usr/bin/env python
#coding=utf-8
#__author__:Administrator
#__date__:2017/7/20

from functools import reduce

#函数

#不定长参数，接收的是元组
def add(*args):
    print(args)
    sum=0
    for i in args:
        sum+=i
    print(sum)

add(1,2,3,4)


#不定长参数，接收的是字典

def print_info(name,age,sex,*args,**kwargs):
    print(kwargs)
    for i,v in kwargs.items():
        print(i,v)
    print(name)
    print(age)
    print(sex)
    print(args)

#形参从左到右(位置参数，关键字参数，可变长参数(元组),可变长参数(字典))
print_info('alex',23,'male',1,2,3,jobs='IT',hobby='girls')

#注意点：1.函数里面如果没有return，就会返回none 2.如return里有多个对象，则返回一个元组


#函数作用域
#4个
#内建作用域  优先级 高
#全局作用域
#enclosing作用域
#局部作用域  优先级 低

#嵌套函数中nonclocal变量会覆盖enclosing层的变量
#函数中的global变量会覆盖全局作用域的变量


def outer():
    x=11
    def inner():
        nonlocal x
        x=123
        print(x)
    inner()
    print(x)

# outer()


#递归函数

def factorial(number):
    ret=1
    for i in range(1,number+1):
        ret=ret*i

    return ret


# print(factorial(5))


def factorial_new(number):
    if number==1:
        return 1
    return number*factorial_new(number-1)


print(factorial_new(5))

#关于递归的特性：
#1调用自身函数
#2有一个结束条件

#效率低
#凡是用递归可以写的时候可以用循环解决

# def Fibonacci(n):
#     before=0
#     after=1
#     for i in range(1,n):
#         ret=before+after
#         before=after
#         after=ret
#     return ret

# print(Fibonacci(6))

def Fibonacci_new(n):
    if n==1 or n==0:
        return n
    return Fibonacci_new(n-1)+Fibonacci_new(n-2)

print(Fibonacci_new(8))


#重要内置函数
#作用到过滤出的元素上
#filter()
#作用到每一个元素上
#map()
#作用到每一个元素上并相加
#reduce() 使用方法之前 from functools import reduce ,注意return是一个值，不是迭代器


print(map(lambda a,b : a*b,range(1,11)))

#高阶函数
#函数名可以作为返回值
#函数名可以当参数输入

