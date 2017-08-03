#!/usr/bin/env python
#coding=utf-8
#__author__:Administrator
#__date__:2017/7/25


import random

def consumer():
    while True:
        data=yield
        print('消费了',data)

def producer():
    while True:
        data=random.randint(1,9)
        print('生产了', data)
        yield data



def circle(jobs,consumer,producer):
    c=consumer()
    p=producer()
    next(c)
    for i in range(1,jobs):
        data=next(p)
        c.send(data)

circle(5,consumer,producer)

