#!/usr/bin/env python
#coding=utf-8
#__author__:Administrator
#__date__:2017/8/5

import socket,os
#客户端


#connect
#recv()
#send()
#sendall()
#close()

#创建socket对象
sk2=socket.socket()

address=('127.0.0.1',8010)
sk2.connect(address)

base_dir=(os.path.dirname(os.path.abspath(__file__)))

# data=sk2.recv(1024) #接收数据
# print(str(data,'utf8'))
while True:
    inp=input('>>>').strip()
    cmd,relativepath=inp.split('|') #此处要注意  post | 后面的相对路径 可能是文件夹下的 路径  类似 alex/11.png
    path=os.path.join(base_dir,relativepath)#绝对路径+相对路径文件名的拼接
    filename=os.path.basename(path)#此处获取到的是真实的文件名
    file_size=os.stat(path).st_size#此处获取文件的大小
    file_info='post|%s|%s'%(filename,file_size)#最后file_info中包含文件路径和文件大小

    sk2.sendall(bytes(file_info,'utf8'))

    with open(path,'rb') as f:
        has_sent=0
        while has_sent!=file_size:
            data=f.read(1024)
            sk2.sendall(data)
            has_sent+=len(data)
        print('上传成功')


sk2.close()