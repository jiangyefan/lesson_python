#!/usr/bin/env python
#coding=utf-8
#__author__:Administrator
#__date__:2017/8/6

import socket


ip_port = ('127.0.0.1',8011)
sk = socket.socket()
sk.connect(ip_port)
print ("客户端启动：")
while True:
    inp = input('>>>')
    sk.sendall(bytes(inp,"utf8"))
    server_response=sk.recv(1024)
    print (str(server_response,"utf8"))
    if inp == 'exit':
        break
sk.close()