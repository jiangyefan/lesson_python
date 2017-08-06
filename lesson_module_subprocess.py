#!/usr/bin/env python
#coding=utf-8
#__author__:Administrator
#__date__:2017/8/5

import subprocess

a=subprocess.Popen('dir',shell=True,stdout=subprocess.PIPE)
print(str(a.stdout.read(),'gbk'))