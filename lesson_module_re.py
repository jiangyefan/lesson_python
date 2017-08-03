#!/usr/bin/env python
#coding=utf-8
#__author__:Administrator
#__date__:2017/7/26

import re


# print(re.findall('a*?','aa')) #特别要主要 容易匹配到空字符串   ['a', '', '', '', '']
# print(re.findall(r'a{1,3}b','aaaab'))
# print(re.findall('[1-9a-zA-Z]','12tyAs'))
# print(re.findall('[1-9,a-z,A-Z]','12tyAs'))
# print(re.search(r'I','I am I amId'))
# print(re.search(r'(?P<id>\\)','Ia\m').group('id')) #分组命名
# ret=re.search('(asd)+.*(asd)+','asd123asd') #分组命名
# print(ret.groups())
# print(re.search('\([^()]+\)','((1+3))').group())
#
# # [-\^]  #中括号中这些代表功能
#
# print(re.sub('a..x','s.....b','djksaaxbl'))
#
# #findall():所有结果都返回到一个列表里
# #search():返回第一个对象，对象可以调用group()返回结果
# #match():从字符串开始完全匹配，也用group()返回
#
# # ret=re.search('.*','123alex123')
# # print(ret.group())
#
# ret=re.search('(?P<name>\d{2})','123nji')
# print(ret.group('name'))
#
# ret1=re.sub('\d','abc','abc1abc2',1)
# print(ret1)
#
#
# ret2=re.subn('\d','abc','abc1abc2',1)
# print(ret2)
#
# ret3=re.compile('\d{3}')
# print(ret3.findall('5555'))
#
# ret4=re.finditer('\d','ds3sy34')
# print(next(ret4))
# print(next(ret4))


s='((3+4)*2)'
print(re.findall('[^()]+',s))


s1='zhao:90 li:50'

def mysub(m):
    s=m.group()
    s=int(s)
    if s>60:
        return 'PASS'
    else:
        return 'No Pass'

print(re.sub('\d\d',mysub,s1))


print(re.match(r'([1-9]?\d$)|(100)','100').groups())


print(re.findall(r'(?:abc){2}','abcabc'))



