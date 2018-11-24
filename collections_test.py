#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/21 19:12
# @Author  : hearecho
# @Site    : 
# @File    : collections_test.py
# @Software: PyCharm

from collections import namedtuple,deque,defaultdict,OrderedDict,Counter


# namedtuple('名称', [属性list])
Point = namedtuple('point',['x','y'])
p = Point(1,2)
print()
print(p.x,p.y)

#deque 双向列表

q = deque(['a','b','c'])
q.append(1)
q.appendleft(2)
print(q.pop())
print(q)

#defaultdict  如果引用的key不存在 会返回设置的默认值

dd = defaultdict(lambda :'N/A')
dd['1'] = 1
print(dd['1'])
print(dd['2'])

#orderedDict 有序的词典 按照插入的顺序
'''
    3.6之后一般创建的字典也是有序的
'''
d = dict([('a',1),('b',2),('c',3)])
print("无序的字典:",d)
od = OrderedDict([('a',1),('c',2),('b',3)])
print("有序的字典:",od)
#实现先进先出

#Counter 计数器
c = Counter()
for ch in 'programing':
    c[ch] = c[ch] + 1
print(c)