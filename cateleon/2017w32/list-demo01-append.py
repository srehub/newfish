#!/usr/bin/python
# encoding:utf-8

"""
@author: yuanxin after Dean
contact:
@file: 2017/8/10-list-demo01-append.py
@time: 2017/8/10 
"""

aList = []

for i in range(0, 50):
    if ( i%8 == 0 ):
        aList.append(i)
        print("the i in list is :  ", (aList))   # print the list if the condition is true
    print("the i in list is :  ", (aList))       # print the list anyway
print("While, the list is :  ", (aList))         # print the list after the circulation

for var in aList:
    print(var)
    if var <= 16:
        index = aList.index(var)                 #  use index() to find the index of object 16
        print("index is: ", (index))             #  index is:  2
        print("Now, I'm going to change it!")
        aList[index] = "Hello "                  #  chanage aList[2] to "Hello"

if __name__ == '__main__':
    print("Now, the list is : ", (aList))
