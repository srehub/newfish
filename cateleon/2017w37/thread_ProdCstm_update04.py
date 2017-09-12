#!/usr/bin/python
# encoding:utf-8

"""
@author: yuanxin
contact:
@file: 2017/9/13-thread_ProdCstm_demo01.py
@time: 2017/9/13 
"""

"""
框架搭好之后，开始在框架内添加内容；
首先，需要在构造函数里添加2个参数，队列和锁
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
            self._lk.acquire()
            self._ml.append(msg)
            self._lk.notify_all()
            self._lk.release()
            i += 1
            time.sleep(0.5)
            print(msg)

class Cstm(Thread):

    def __init__(self,msglist,lk):
        Thread.__init__(self)
        self._ml = msglist
        self._lk = lk

    def run(self):
        while True:
            self._lk.acquire()
            while len(self._ml) == 0:
                self._lk.wait()
            msg = self._ml.pop()
            self._lk.release()
            print("Cstm %s receive: %s" % (current_thread(),msg))
            time.sleep(0.8)
            # print(msg)

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