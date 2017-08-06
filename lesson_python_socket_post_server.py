#!/usr/bin/env python
#coding=utf-8
#__author__:Administrator
#__date__:2017/8/5




import socket
import subprocess
import os

#服务端

# bind()
# listen()
# accept()
#recv()
#send()
#sendall()
#close()

#family三个参数
#AF_INET:IPV4
#AF_INET6：IPV6
#AF_UNIX

#TYPE两个参数
#sock_stream tcp
#sock_dgram udp

#创建socket对象
sk=socket.socket()

address=('127.0.0.1',8010)
#参数需要元组，绑定ip和端口
sk.bind(address)

#socket连接数量，此为同时3人连接
sk.listen(3)
base_dir=(os.path.dirname(os.path.abspath(__file__)))

conn,addr=sk.accept()
while True:
    try:

        data=conn.recv(1024)
    except Exception:
        conn, addr = sk.accept()
        data = conn.recv(1024)
    if data:
        print(str(data,'utf8')) #这里切记要转换
        cmd,filename,filesize=str(data,'utf8').split('|')
        path=os.path.join(base_dir,'jiang',filename)#拼接绝对路径
        filesize=int(filesize)

        with open(path,'ab') as f:
            has_receive=0
            while has_receive!=filesize:
                data=conn.recv(1024)
                f.write(data)
                has_receive+=len(data)



sk.close()
