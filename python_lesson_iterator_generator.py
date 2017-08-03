#!/usr/bin/env python
#coding=utf-8
#__author__:Administrator
#__date__:2017/7/23

#列表生成式
# a=[x*x for x in range(1,100)]
# print(a)

# def diy_pow(number):
#     return number**3
#
# a=[diy_pow(number) for number in range(1,101)]
# # print(a)


#生成器初识
#() 注意和列表生成式的区别[]
# my_generator=(x for x in range(1,101))
# print(my_generator) #<generator object <genexpr> at 0x000001F98BEB3B48>
#
#
# print(next(my_generator)) #等价于my_generator.__next__()  in py2:s.next()
# print(my_generator.__next__())

#生成器两种创建方式
#生成器就是创建一个可迭代对象
#1.(xxx for xxx in seq)
#2.yield关键字

# def foo():
#     print('ok')
#     yield 1
#     print('ok2')
#     yield 2
#     return None
#
# f=foo()
# print('*'*50)
# f.__next__()  #迭代器执行打印OK
# f.__next__()  #从yield行开始迭代器继续执行打印OK2
#
# ret=f.__next__()  #迭代器执行打印OK后碰到yield 1后返回1
# ret2=f.__next__()  #迭从yield行开始迭代器继续执行打印OK2后碰到yield 2后返回2


# def fabonacci(num):
#     before=0
#     after=1
#     for i in range(1,num):
#         yield before
#         before,after=after,before+after
#
#
#
# fabonacci_iter=fabonacci(100)
#
# print(fabonacci_iter.__next__())


#send方法

# def foo():
#     print('ok')
#     count=yield 1
#     print(count)
#     print('ok2')
#     yield 2
#     return None
#
# f=foo()
# print('*'*50)
#
# print(f.send(None))  #next(b) 第一次send前如果没有next，只能传一个send(None)
# print(f.send('eee'))


#迭代器
#满足两个条件：1.有iter方法 2.有next方法

#for i in [2,3,4]
#内部三件事 1.调用iter([2,3,4]) 2.不断调用next方法 3.处理stopiteration异常


#找出文件中字数最多的一行
print(max(len(x.strip()) for x in open('c:\\123.txt','r+')))
