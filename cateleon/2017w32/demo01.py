#!/usr/bin/python
# encoding:utf-8 | #-*-coding:utf8-*- | coding:utf8
 
import time
"""
@author: 
contact:
@file: demo01.py
@time: 2017/7/30 
"""
class Student:
    def __init__(self, name, friend):
        self.name = name
        self.friend = friend
        print("after school, "+ self.name +" go home.")
 
    def doHomeWork(self):
        print(self.name +" do his homework self.")
 
    def playWithFriend(self):
        for i in range(9):
            time.sleep(1)
            print( i+1 , " times")
            print(self.name + " play games with his friend " + self.friend)
 
    def sleep(self):
        print("sleeping......")
 
if __name__ == "__main__":
    tom = Student("tom", "jack")
    tom.doHomeWork()
    tom.playWithFriend()
    tom.sleep()