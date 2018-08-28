#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/28 19:25
# @Author  : hearecho
# @Site    : 
# @File    : FilterStudy.py
# @Software: PyCharm

'''
    过滤列表中的元素

'''
import random
class FilterStudy():
    def __filter(self):
        a = []
        for i in range(10):
            a.append(random.randint(0,100))
        print(a)
        less_twenty = list(filter(lambda x:x<20,a))
        print(less_twenty)

    def test(self):
        self.__filter()
    pass

if __name__ == '__main__':
    filter1= FilterStudy()
    filter1.test()