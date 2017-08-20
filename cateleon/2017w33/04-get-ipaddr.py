#!/usr/bin/python
# encoding:utf-8

"""
@author: yuanxin
contact:
@file: 2017/8/19-04-get-ipaddr.py
@time: 2017/8/19 
"""

import socket
def getLocalIp():
    """
    获取本机IP地址
    :return:
    """
    try:
        csock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        csock.connect(('8.8.8.8',80))
        (addr, port) = csock.getsockname()
        csock.close()
        return addr
    except(socket.error):
        return '127.0.0.1'

if __name__=="__main__":
    IPADDR = getLocalIp()
    print(IPADDR)