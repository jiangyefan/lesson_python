#!/usr/bin/env python
#coding=utf-8
#__author__:Administrator
#__date__:2017/7/29

import shelve

f=shelve.open(r'c:\\shelve.txt')

f['info']={'name':'alex','age':'18'}

print(f.get('info'))





