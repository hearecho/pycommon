#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/22 14:33
# @Author  : hearecho
# @Site    : 
# @File    : thread线程.py
# @Software: PyCharm

import time,threading

def loop():
    print('thread %s is running.....' % threading.current_thread().name)
    n = 0
    while n<5:
        n = n+1
        print('thred %s >> %s' %(threading.current_thread().name,n))
    print('thred %s ended.' %threading.current_thread().name)


if __name__ == "__main__":
    print('thread %s is running ....'% threading.current_thread().name)
    t = threading.Thread(target=loop,name = 'LoopThread')
    t.start()
    t.join()
    print('thread %s ended' % threading.current_thread().name)