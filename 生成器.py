#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/28 16:25
# @Author  : hearecho
# @Site    : 
# @File    : 生成器.py
# @Software: PyCharm
'''
    包含三个部分: 可迭代对象，迭代器，迭代

'''

class Generators():

    '''
        简单的生成器
    '''
    def __generator_func(self):
        for i in range(10):
            yield i
    '''
        计算斐波那契数列的⽣成器
    '''
    def __fibon(self,n):
        a=b=1
        for i in range(n):
            yield a
            a,b=b,a+b


    def test(self):
        # for i in self.__generator_func():
        #     print(i)
        # __fibon()是一个生成器   <class 'generator'>
        # print(type(self.__fibon(2)))
        for x in self.__fibon(100):
            print(x)

    pass

if __name__ == '__main__':
    generator = Generators()
    generator.test()