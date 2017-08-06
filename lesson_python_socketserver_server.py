#!/usr/bin/env python
#coding=utf-8
#__author__:Administrator
#__date__:2017/8/6

import socketserver

class MyServer(socketserver.BaseRequestHandler): #继承BaseRequestHandler

    def handle(self): #多态改写父类方法
        print('服务端启动....')
        while True:
            conn=self.request   #conn,addr=sk.accept()  一样
            print(self.client_address)
            while True:
                client_data=conn.recv(1024)
                print(str(client_data,'utf8'))
                print('waiting...')
                server_response=input('>>>')
            conn.close()


if __name__=='__main__':
    server=socketserver.ThreadingTCPServer(('127.0.0.1',8011),MyServer)
    server.serve_forever()