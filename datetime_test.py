#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/21 17:33
# @Author  : hearecho
# @Site    : 
# @File    : datetime_test.py
# @Software: PyCharm

from datetime import datetime,timedelta
import time

#-----------*返回当前时间*------------
now = datetime.now()
print(now)

#-----------*指定时间日期*------------
dt = datetime(2015,4,19,12,20)
print(dt)

#-----------*datetime转换为timestamp*-
print(now.timestamp())
print(time.time())

#-----------*timestamp转换为datetime*-
#utc + 8 等于本地时间 即 北京时间
t = 1564864535.65
print('转换为本地时间为:',datetime.fromtimestamp(t))
print('转换为UTC时间为:',datetime.utcfromtimestamp(t))

#---------*str转换为datetime*----------
#补位0
cday = datetime.strptime('2015-5-6 18:9:59', '%Y-%m-%d %H:%M:%S')
print(cday)

#---------*datetime转换为str*----------
print(now.strftime('%a,%b %d %H:%M'))

#---------*datetime加减 timedelta*-----
print('小时加10',now + timedelta(hours=10))
print('day +1',now+timedelta(days=1))
print('days-1 hours-10',now-timedelta(days=1,hours=10))


