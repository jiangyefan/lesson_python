#!/usr/bin/env python
#coding=utf-8
#__author__:Administrator
#__date__:2017/8/2


class Foo:
    a=123
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        return  "%s-%s"%(self.name,self.age)

obj=Foo('alex',19)

print(obj.__dict__)

getattr(obj,'name')#反射查找对象成员变量方法
setattr(obj,'k1','v1')  #反射的塞值方法
hasattr(obj,'k1')#反射查找对象中是否有此成员变量
print(obj.__dict__)
delattr(obj,'k1')
print(obj.__dict__)#反射中删除成员变量方法



