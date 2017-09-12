#!/usr/bin/python
# encoding:utf-8

"""
@author: yuanxin
contact:
@file: 2017/9/13-thread_ProdCstm_demo01.py
@time: 2017/9/13 
"""

"""
创建一个生产者、消费者的模型； 先搭框架，不实现任何功能；
"""

from threading import Thread,Condition,current_thread
import time

class Prod(Thread):

    def __init__(self):
        pass

    def run(self):
        pass

class Cstm(Thread):

    def __init__(self):
        pass

    def run(self):
        pass

# 实现测试代码，首先有一个队列缓冲区，使用列表表示；
# 其次生产者消费者模型，需要一个 Condition 全局锁；
if __name__=='__main__':
    msglist = []
    lk = Condition()

    prod1 = Prod(msglist,lk)
    prod1.start()

    cstms = [Cstm(msglist,lk) for i in range(4)]
    for c in cstms:
        c.start()

    prod1.join()
    for c in cstms:
        c.join()