#!/usr/bin/python
# encoding:utf-8

"""
@author: yuanxin
contact:
@file: 2017/8/16-web-server-demo01.py
@time: 2017/8/16 
"""

import sys
import socket

HOST = None
PORT = 8888
skt = None

for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
    af,socktype,proto,canonname,sa = res
    try:
        skt = socket.socket(af,socktype,proto)
    except(socket.error,err_msg):
        print(err_msg)
        skt = None
    try:
        skt.bind(sa)
        skt.listen(1)
    except(socket.error,err_msg):
        print(err_msg)
        skt.close()
        skt = None
        continue
    break
if skt is None:
    print('Could not open socket')
    sys.exit(1)

conn, addr = skt.accept()
print('Connected by', addr)

while 1:
    data = conn.recv(1024)
    if not data: break
    conn.send(data)
conn.close