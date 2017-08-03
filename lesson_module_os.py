#!/usr/bin/env python
#coding=utf-8
#__author__:Administrator
#__date__:2017/7/25


import os

print(os.getcwd())#当前python脚本目录(不包括文件名)
# print(os.chdir('d:\\'));print(os.getcwd())#当前python脚本目录(不包括文件名)

# print(os.curdir)#1个点（当前目录）
# print(os.pardir)#2个点（上一级目录）

# print(os.makedirs('c:\\123\\123'))#创建空文件夹（递归）
# print(os.removedirs('c:\\123\\123'))#删除空文件夹（递归）（有内容删不了）


# print(os.mkdir('c:\\123'))#创建单个文件夹
# print(os.rmdir('c:\\123'))#删除当个文件夹

# print(os.listdir('c:\\'))#类似linux ls命令
# print(os.remove())#类似Linux rm 命令(但只能删文件)

# print(os.rename())#重命名文件

# print(os.stat('c:\\123.txt'))#显示文件信息(时间，大小)

# print(os.sep)#显示系统路径分隔符

# print(os.linesep)#换行分隔符
#
# print(os.pathsep)#多个文件分隔符
#
# print(os.name) #win显示NT linux显示posix
#
# print(os.system('dir'))#调用系统命令
#
# print(os.environ)#显示系统环境变量
#
# print(os.path.abspath())#显示绝对路径
#
# print(os.path.split())#显示元组 linux dirname和basename

# print(os.path.dirname('c:\\123.txt'))#类似linux dirname
#
# print(os.path.basename('c:\\123.txt'))#类似Linux basename
#
# print(os.path.isXXX)#显示是否是xxxx

print(os.path.join('home','linux')) #路径拼接

print(os.path.getatime())#显示该文件访问时间
print(os.path.getmtime())#显示改文件修改时间





