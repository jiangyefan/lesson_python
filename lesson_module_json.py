#!/usr/bin/env python
#coding=utf-8
#__author__:Administrator
#__date__:2017/7/29

import json

# dic={'name':'alex','age':'18'}
#
# dic_to_str=json.dumps(dic)
# with open('c:\\json.text','w')as f:
#     f.write(dic_to_str)


with open('c:\\json.text','r')as f1:
    json_to_dict=json.load(f1)

print(type(json_to_dict))



