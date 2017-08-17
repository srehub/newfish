#!/usr/bin/python
# encoding:utf-8

"""
@author: yuanxin
contact:
@file: 2017/8/16-web-client-demo01.py
@time: 2017/8/16 
"""

import socket
import sys
import os

HOST = '127.0.0.1'
PORT = '8888'
skt = None

for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af,socktype,proto,canonname,sa = res
    try:
        skt = socket.socket(af, socktype, proto)
    except(socket.error):
        print('01', socket )
        skt = None
        continue
    try:
        skt.connect(sa)
    except(socket.error):
        print('02',socket.error)
        skt.close()
        skt = None
        continue
    break
if skt is None:
    print("03", "Could not open socket")
    sys.exit(1)

skt.sendall('Hello, world')
data = skt.recv(1024)
skt.close()
print("04", 'Received', repr(data))
