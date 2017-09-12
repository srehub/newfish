#!/usr/bin/python
# encoding:utf-8

"""
@author: yuanxin
contact:
@file: 2017/9/13-thread_ProdCstm_demo01.py
@time: 2017/9/13 
"""

"""
demo02 中1个生产的 ID 有 4个 消费者；
代码继续优化
"""

from threading import Thread,Condition,current_thread
import time

class Prod(Thread):

    def __init__(self,msglist,lk):
        Thread.__init__(self)
        self._ml = msglist
        self._lk = lk

    def run(self):
        i = 0
        while True:
            msg = " Prod msg is : %s " % i
            self._ml.append(msg)
            i += 1
            time.sleep(0.6)
            print(msg)

class Cstm(Thread):

    def __init__(self,msglist,lk):
        Thread.__init__(self)
        self._ml = msglist
        self.lk = lk

    def run(self):
        while True:
            msg = self._ml.pop()
            time.sleep(0.6)
            print("Cstm %s receive : %s" % (current_thread(),msg))

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