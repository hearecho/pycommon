#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/30 11:14
# @Author  : hearecho
# @Site    : 
# @File    : decorator.py
# @Software: PyCharm
# 本质上，它是一个高阶函数，以被装饰的函数（比如上面的 hello）为参数，
# 并返回一个包装后的函数（比如上面的 wrapped）给被装饰函数（hello）。
def decorator_one(func):
    def wrapped1():
        return "<i>"+func()+"</i>"
    return wrapped1

def decorator_two(func):
    def wrapped2():
        return "two   "+func()
    return wrapped2

@decorator_one
@decorator_two
def hello():
    return "helloworld"

# decorator.hello.__name__   为 wrapped
#两个装饰器相当于decorator_one(decorator_two(func))

#带参数的装饰器 需要装饰器 里面的函数 也要做出一些该变
# eg
def decorator_three(func):
    def wrapped3(*args,**kwargs):
        ret = func(*args,**kwargs)
        return 'three\t'+ret
    return wrapped3

@decorator_three
def hello_args(name):
    return 'hello %s' %name

@decorator_three
def hello_args2(name1,name2):
    return '{} say hello to {}'.format(name1,name2)