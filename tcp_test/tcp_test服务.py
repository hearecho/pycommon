#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/23 9:59
# @Author  : hearecho
# @Site    : 
# @File    : tcp_test服务.py
# @Software: PyCharm

import socket
import time,threading


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#监听端口
s.bind(('127.0.0.1',9001))

#等待连接
s.listen(5)#参数是等待连接的最大数量


def tcplink(sock,addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

if __name__ == '__main__':
    while True:
        socket, addr = s.accept()

        # 创建新线程处理Tcp连接
        t = threading.Thread(target=tcplink, args=(socket, addr))

        t.start()