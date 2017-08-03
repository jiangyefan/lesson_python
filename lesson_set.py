#!/usr/bin/env python
#coding=utf-8
#__author__:Administrator
#__date__:2017/7/20

#集合
#无序不重复
#要求里面对象是可哈希的(Int str tuple)
#但是set整体是非可哈希的不能作为键值，frozenset可以作为键值
my_set=set([3,'3',3])
#集合中添加元素
my_set.add(123)
print(my_set)
#集合中添加序列
my_set.update([123,'1'])
print(my_set)
#集合中删除元素
my_set.remove(123)
print(my_set)
#集合中随机删除元素，并返回
a=my_set.pop()
print(my_set)
#清空该集合
my_set.clear()
print(my_set)
#删除该集合
# del my_set


#高级
#操作符

a=set([1,2,3,4])
b=set([1,2,3,4,5])
#并集  a与b联合后去重
print(a.union(b))
print(a|b)
#交集  a与b共有的部分
print(a.intersection(b))
print(a&b)
#差集 b里面有，a里面没有
print(b.difference(a))
print(b-a)
#对称差集 a与b除交集以外部分 反向交集
print(b.symmetric_difference(a))
print(b^a)

