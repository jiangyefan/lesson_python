#!/usr/bin/env python
#coding=utf-8
#__author__:Administrator
#__date__:2017/7/31

# python中多继承
#
# 左侧优先找
# 如果第二参数跟第一参数是同一个根时候，根最后执行

# class father:
#     def first(self):
#         print('ok father')
#
# class son(father):
#     def first(self):
#         super(son,self).first() #执行父类方法 first方法  里面两个参数1.子类名字 2.self
#         father.first(self)  #第二种方法 执行父类方法
#         print('ok son')
#
#
# class f0:
#     def first(self):
#         print('ok f0')
#
# class f1(f0):
#     def first1(self):
#         print('ok f1')
#
# class f2(f0):
#     def first(self):
#         print('ok f2')
#
# class s(f1,f2):
#     pass
#
# obj=s()
# obj.first()
#
# #多继承中，如果左边类中有，则执行左边类中方法，如没有看是否继承父级，一直找到头，如没有继承父类，则找右边类中是否有方法，2.左右类最终都继承与一个父类的情况下，先遵循左边原则，找到最后除父类外都没有该方法，则开始找右边类中是否有方法如有则执行，如没有再执行父类方法(敲黑板)
#
#
# #对于__init__继承的情况，也遵循左边原则，可以用super（obj，self）或者父类.__init__(obj)
#
#
# #成员修饰符
#
# class Foo:
# #私有变量的情况
#     __v='123' #类私有变量
#
#     def __init__(self,name,age):
#         self.name=name
#         # self.age=age
#         self.__age=age  #私有变量，无法通过对象直接访问 需要通过内部方法去间接访问
#
#     def show(self):
#         # return  self.__age
#         return  Foo.__v
#
#
#     @staticmethod
#     def stat():
#         return Foo.__v
#
#     @classmethod
#     def clss(cls):
#         return Foo.__v
#
# #私有方法的情况
#     def __f1(self):
#         return 345
#
#     def f2(self):
#         ret=self.__f1()  #通过其他方法间接去执行私有方法
#         return ret
#
#
# obj=Foo('alex',19)
# print(obj.show())
# print(Foo.stat())
# print(Foo.clss())
#
# print(obj.f2())
#
# # print(Foo.__v)#不能通过此方法调用类私有变量    需要通过这种方式 return  Foo.__v
#
#
# #私有变量与方法在类继承的情况
#
# class F:
#     def __init__(self):
#         self.__ge=123
#
#     def show1(self):
#         print(self.__ge)
#
# class S(F):
#     def __init__(self,name):
#         self.name=name
#         self.__age=18
#         super(S, self).__init__()
#
#     def show(self):
#         print(self.name)
#         print(self.__age)
#         # print(self.__ge)  #子类不能访问父类的私有变量
#         self.show1()   #调用父类的方法间接去访问父类的私有变量
# s=S('alex')
# s.show()


class Foo:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __call__(self, *args, **kwargs):
        print('call')

    def __int__(self):
        return 111

    # def __str__(self):
    #     return 'alex'

    def __add__(self, other):  #self 是 obj   other 是 obj2
        # return self.age+other.age
        return Foo(other.name,self.age)

    def __del__(self): #对象销毁的时候自动执行，析构方法 ，至于什么时候销毁，课程中未提及
        print('析构方法')

    def __getitem__(self, item):  #例子：li[8]列表取索引的实现
        pass
    def __setitem__(self, key, value):#例子 li[8]=xxx
        pass

    def __delitem__(self, key):#例子 del li[8]
        pass



obj1=Foo('alex',19)
obj2=Foo('eric',18)
obj1()#对象加括号是执行 __call__方法

print(obj1[9])

# print(int(obj)) #int类里面塞个对象会执行内部的__int__方法 不常用
# print(str(obj)) #str类里面塞个对象会执行内部的__str__方法 一般用于打印一下对象内部情况
# print(obj)#同上

# 定制类
#
# __init__   class()
# __int__    int(obj)
# __call__  obj()
# __str__   print(obj) str(obj)
#__add__ #两个对象相加时，自动执行第一个对象的 __add__方法，并且将第二个对象当参数传递进来

#__del__ #对象销毁的时候自动执行，析构方法 ，至于什么时候销毁，课程中未提及
#__dict__#对象和类中有哪些成员



r=obj1+obj2
print(r.name)
print(r.age)

#两个对象相加时，自动执行第一个对象的 __add__方法，并且将第二个对象当参数传递进来





