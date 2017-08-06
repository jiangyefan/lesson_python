#!/usr/bin/env python
#coding=utf-8
#__author__:Administrator
#__date__:2017/8/5

class Foo:

    __v=None

    @classmethod
    def get_instance(cls):
        if cls.__v:
            return cls.__v
        else:
            cls.__v=Foo()
            return cls.__v

# obj=Foo() #obj对象，obj也改为Foo类的实例(实例化)
# #单例，永远使用同一份对象





