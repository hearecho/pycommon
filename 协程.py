#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/23 10:50
# @Author  : hearecho
# @Site    : 
# @File    : 协程.py
# @Software: PyCharm

#yield 返回

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1

        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)