#!/usr/bin/env python
#coding=utf-8
#__author__:Administrator
#__date__:2017/7/25

import hashlib

password=hashlib.md5() #创建一个md5对象
password.update('hello world'.encode('utf8'))  #对helloworld 加密
print(password.hexdigest()) #5eb63bbbe01eeed093cb22bb8f5acdc3  #16进制加密

password.update('alex'.encode('utf8'))  #对helloworldalex 加密  注意！此处是与之前加密的操作有关联
print(password.hexdigest())




new_password=hashlib.sha256()

new_password.update('hello world'.encode('utf8'))
print(new_password.hexdigest())