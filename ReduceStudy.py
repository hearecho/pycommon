#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/28 19:43
# @Author  : hearecho
# @Site    : 
# @File    : ReduceStudy.py
# @Software: PyCharm
'''
    前面产生的结果回对后续列表元素继续应用

'''
from functools import reduce
class ReduceStudy():
    def __reduce(self):
        product = reduce((lambda x,y:x*y),[1,2,3,4])
        print(product)

    def test(self):
        self.__reduce()

    pass

if __name__ == '__main__':
    reduce1 = ReduceStudy()
    reduce1.test()