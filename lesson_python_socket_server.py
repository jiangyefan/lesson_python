#!/usr/bin/env python
#coding=utf-8
#__author__:Administrator
#__date__:2017/8/5




import socket
import subprocess

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


conn,addr=sk.accept()
while True:
    try:

        data=conn.recv(1024)
    except Exception:
        conn, addr = sk.accept()
        data = conn.recv(1024)
    if data:
        print(str(data,'utf8')) #这里切记要转换
        obj = subprocess.Popen(str(data,'utf8'), shell=True, stdout=subprocess.PIPE)#tdout=subprocess.PIPE此参数是将此进程显示的结果管道到主进程上
        cmd_ret=obj.stdout.read()
        # print('waiting......')
        # inp=input('>>>')
        # conn.send(bytes(inp,'utf8'))  #发送数据
        result_len=bytes(str(len(cmd_ret)),'utf8')#先获取命令结果的长度
        conn.sendall(result_len)#传长度
        conn.sendall(cmd_ret)#传实际结果
    else:
        conn.close()
        conn,addr=sk.accept()  #server端不关闭继续接收其他客户端请求
        continue


sk.close()
