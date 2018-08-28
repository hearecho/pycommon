#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/28 16:03
# @Author  : hearecho
# @Site    : 
# @File    : argAndkwargs.py
# @Software: PyCharm

'''
    *args 相当于传入的是一个列表
    **kwargs 相当于传入的是一个字典

'''
class Test():
    def __init__(self):
        super()

    @staticmethod
    def testArgs(normal_arg,*args):
        print("normal_arg is {}".format(normal_arg))
        for x in args:
            print("another	arg	through	*argv:",x)
    @staticmethod
    def testKwargs(normal_arg,**kwargs):
        print("normal_arg is {}".format(normal_arg))
        for k,v in kwargs.items():
            print("key: ",k+" value: ",v)

if __name__ == '__main__':
    test = Test()
    args = ["python","java","go"]
    kwargs = {"python":2,"java":1,"go":3}

    test.testArgs("normal",*args)
    test.testKwargs("normal",**kwargs)


