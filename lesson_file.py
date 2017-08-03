#!/usr/bin/env python
#__author__:Administrator
#__date__:2017/7/16
import os
import stat

# #看文件是否存在，是否可读，可写，可执行
# ret=os.access('c:\\123.txt',os.F_OK)
# print(ret)
# ret=os.access('c:\\123.txt',os.R_OK)
# print(ret)
# ret=os.access('c:\\123.txt',os.W_OK)
# print(ret)
# ret=os.access('c:\\123.txt',os.X_OK)
# print(ret)

# #切换工作路径
# os.chdir('d:\\')
# ret=os.getcwd()
# print(ret)
# os.chdir('c:\\')
# ret=os.getcwd()
# print(ret)

#设置权限
# os.chmod('c:\\123.txt',stat.S_IROTH)
# os.chmod('c:\\123.txt',stat.S_IWOTH)
# os.chmod('c:\\123.txt',stat.S_IXOTH)
# os.chmod('c:\\123.txt',stat.S_IRWXO)
#
# os.chmod('c:\\123.txt',stat.S_IRGRP)
# os.chmod('c:\\123.txt',stat.S_IWGRP)
# os.chmod('c:\\123.txt',stat.S_IXGRP)
# os.chmod('c:\\123.txt',stat.S_IRWXG)
#
# os.chmod('c:\\123.txt',stat.S_IRUSR)
# os.chmod('c:\\123.txt',stat.S_IWUSR)
# os.chmod('c:\\123.txt',stat.S_IXUSR)
# os.chmod('c:\\123.txt',stat.S_IRWXU)
#
# os.chmod('c:\\123.txt',stat.S_ISVTX)


#修改属组 属主
# os.chown('c:\\123.txt',100,-1)

#修改更目录
# os.chroot('c:\\')


#展示目录下文件
# print(os.listdir('c:\\'))

#展示目录下文件
# 注意方法名不一样mkdir和makedirs
# print(os.mkdir('c:\\123',0777))
# os.makedirs('c:\\123\\345')


#打开一个文件，并写入
# f=os.open('c:\\555.txt',os.O_RDWR|os.O_CREAT)
# os.write(f,bytes('got it','utf-8'))
# os.close(f)

#重命名文件或目录,删除目录和文件
# os.renames('c:\\555.txt','c:\\666.txt')
# os.remove('c:\\666.txt')

#展示时间
# print(os.utime('c:\\123.txt'))
# file_time=os.stat('c:\\123.txt')
# print(file_time.st_mtime,file_time.st_atime)


f=open('c:\\123.txt','r+',encoding='utf-8')
print(f.tell())
f.write('aaaaa')
f.close()
