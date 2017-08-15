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

HOST = '127.0.0.1'
PORT = '8888'
skt = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af,socktype,proto,canonname,sa = res
    try:
        skt = socket.socket(af, socktype, proto)
    except(socket.error):
        skt = None
        continue
    try:
        skt.connect(sa)
    except(socket.error):
        skt.close()
        skt = None
        continue
    break
if skt is None:
    print("Could not open socket")
    sys.exit(1)

skt.sendall('Hello, Python')
data = skt.recv(1024)
skt.close()
print('Received', repr(data))
