#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/30 10:32
# @Author  : hearecho
# @Site    : 
# @File    : close_packages.py
# @Software: PyCharm
from math import pow,sqrt

# 闭包的最大特点就是引用了自由变量，即使生成闭包的环境已经释放，闭包仍然存在。
#eg 1:
def make_pow(n):
    def inner_func(x):
        return pow(x,n)
    return inner_func

#利用闭包模拟类的实例

class Point(object):
    def __init__(self,x,y):
        self.x,self.y = x,y

    def get_distance(self,u,v):
        distance = sqrt((self.x-u)**2 + (self.y-v)**2)
        return distance

# eg2
def point(x,y):
    def get_distance(u,v):
        return sqrt((x-u)**2+(y-v)**2)
    return get_distance

#闭包函数  误区

# error eg3
def count():
    func = []
    for i in range(1,4):
        def f():
            return i;
        func.append(f)
    return func
# 结果全是 3
# 尽量避免在闭包中引用循环变量，或者后续会发生变化的变量。
# correct eg4
#再增加一个函数来解决 返回一个匿名函数
def count():
    func = []
    for i in range(1,4):
        def g(param):
            f = lambda :param;
            return f;
        func.append(g(i))
    return func