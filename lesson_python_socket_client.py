#!/usr/bin/env python
#coding=utf-8
#__author__:Administrator
#__date__:2017/8/5

import socket
#客户端


#connect
#recv()
#send()
#sendall()
#close()

#创建socket对象
sk2=socket.socket()

address=('127.0.0.1',8011)
sk2.connect(address)

# data=sk2.recv(1024) #接收数据
# print(str(data,'utf8'))
while True:
    inp=input('>>>')
    if inp=='exit':  #客户端输入exit后 退出聊天
        break
    else:
        sk2.send(bytes(inp, 'utf8'))  # 发送数据

        result_len=int(str(sk2.recv(1024),'utf8')) #接收命令结果的长度
        print(result_len)
        data=bytes()#初始一个bytes空类型，以供下面累加
        while len(data)!=result_len:#判断长度是否超过命令结果长度，等于代表接受完

            data += sk2.recv(1024)
        print(str(data, 'gbk'))
            # print(str(data, 'utf8'))
            # data=sk2.sendall(bytes('123','utf8'))

sk2.close()