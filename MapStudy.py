#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/28 18:58
# @Author  : hearecho
# @Site    : 
# @File    : MapStudy.py
# @Software: PyCharm
'''
    Map会将⼀个函数映射到⼀个输⼊列表的所有元素上
    list元素可以是一组函数
    map(func,list)  type--><class 'map'>
'''

class MapStudy():
    def __map(self):
        items = [1,2,3,4,5,6,7]
        print(type(map(lambda x:x**2,items)))
        sq = list(map(lambda x:x**2,items))
        print(sq)

    def __multiply(self,x):
        return x*x

    def __add(self,x):
        return x+x

    # list 为一组函数
    def __maptest2(self):
        funcs =[self.__multiply,self.__add]
        for i in range(5):
            value = list(map(lambda x:x(i),funcs))
            print(value)

    def test(self):
        # self.__map()
        self.__maptest2()


    pass

if __name__ == '__main__':
    map1 = MapStudy()
    map1.test()