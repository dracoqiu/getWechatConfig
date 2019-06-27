#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-09 16:16:21
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import logging
from logging.handlers import TimedRotatingFileHandler
import time

logfilename = '/home/python/wechat_py/logs/' + str(time.strftime('%Y%m%d')) + '.log'
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%d %m %Y %H:%M:%S',
    filename=logfilename,
    filemode='a')

#################################################################################################
# # 定义一个TimedRotatingFileHandler，按时间段写日志，不删除历史日志.服务器定时重启的话请注释这块
# Rthandler = TimedRotatingFileHandler('/home/py/wechat_py/logs/myapp.log', when="D", interval=1, backupCount=0)
# # 设置后缀名称，跟strftime的格式一样
# Rthandler.suffix = "%Y-%m-%d.log"
# Rthandler.setLevel(logging.DEBUG)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# Rthandler.setFormatter(formatter)
# logging.getLogger('').addHandler(Rthandler)
###########################################################################################

#################################################################################################
# 定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
#################################################################################################

# logging.debug('This is debug message by liu-ke')
# logging.info('This is info message by liu-ke')
# logging.warning('This is warning message by liu-ke')
