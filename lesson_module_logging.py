#!/usr/bin/env python
#coding=utf-8
#__author__:Administrator
#__date__:2017/7/25

import logging

# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s [Line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%F %T',
#                     filename='c:\\test.log',
#                     filemode='a')
#
#
# logging.debug('logging debug')
# logging.info('logging info')
# logging.critical('logging critical')
# logging.warning('logging warning')
# logging.error('logging error')


#控制台和文件同时显示

logger=logging.getLogger()
#文件 handler
fh=logging.FileHandler('c:\\test.log')
#console handler
ch=logging.StreamHandler()
#定义格式
formatter=logging.Formatter('%(asctime)s %(filename)s [Line:%(lineno)d] %(levelname)s %(message)s')

ch.setFormatter(formatter)
fh.setFormatter(formatter)

logger.addHandler(ch)
logger.addHandler(fh)


logger.setLevel(logging.DEBUG)

logger.debug('logging debug')
logger.info('logging info')
logger.critical('logging critical')
logger.warning('logging warning')
logger.error('logging error')