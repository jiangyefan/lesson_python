#!/usr/bin/env python
#coding=utf-8
#__author__:Administrator
#__date__:2017/7/26

import configparser

config=configparser.ConfigParser()

config.add_section('default')
config.set('default','serveraliveinterval','45')
config.set('default','compression ','yes')
config.set('default','compressionlevel ','9')

with open('c:\\123.ini','w') as configfile:
    config.write(configfile)


config.read('c:\\123.ini')
print(config.items('default'))
print(config.options('default'))
print(config.sections())


