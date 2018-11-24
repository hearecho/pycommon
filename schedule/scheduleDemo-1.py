#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/24 20:27
# @Author  : hearecho
# @Site    : 
# @File    : scheduleDemo-1.py
# @Software: PyCharm
import time

def task():
    print("do task!!!")

def schedule(n):
    while True:
        print(time.strftime('%Y-%m-%d %X', time.localtime()))
        # 执行任务
        task()
        time.sleep(n)

if __name__ == '__main__':
    schedule(2)