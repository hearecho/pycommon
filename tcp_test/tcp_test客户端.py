#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/23 10:07
# @Author  : hearecho
# @Site    : 
# @File    : tcp_test客户端.py
# @Software: PyCharm

import socket


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect(('127.0.0.1', 9001))
    print(s.recv(1024).decode('utf-8'))
    for data in [b'Michael', b'Tracy', b'Sarah']:
        # 发送数据:
        s.send(data)
        print(s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    s.close()