#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/22 17:00
# @Author  : hearecho
# @Site    : 
# @File    : tcp.py
# @Software: PyCharm

import socket

#创建socket AF_INET 是 ipv4  AF_INET6 为ipv6 SOCK_STREAM指定使用面向流的TCP协议

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#创建连接  传进去的是一个元祖tuple 一个是ip地址 和端口
s.connect(('www.sina.com.cn',80))

#发送数据  发送的文本格式必须符合HTTP标准
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

#接收数据
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
# with open('sina.html', 'wb') as f:
#     f.write(html)
