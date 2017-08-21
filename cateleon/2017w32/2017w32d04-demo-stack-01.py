#!/usr/bin/python
# encoding:utf-8

"""
@author: yuanxin
contact:
@file: 2017/8/11-demo-stack-01.py
@time: 2017/8/11 
"""


list = [ ]
num = 6
for i in range(1,9):
    # print(i)
    if i < num:
        list.append(i)
        print( (list), ", I want" , (num),  "balls, Now there is ", len(list), ", give me one more")
    elif i == num:
        list.append(i)
        print( (list) , ", That's right, I have ", len(list), "balls, great !" )
    else:
        list.append(i)
        print((list), "There are ", len(list) , "balls, it's too many, i will drop", i)
        list.pop()
        print("Still ,i have " ,(list))

# # print(i)
    # print.len(i)    # if i <= 7:
    # pass   # i.pop()
    # print(i)
    # i.pop()
    # print(i)

# from collections import deque
# que = deque([ 'a','b','c','d','e','f' ])
# que.append('g')
# que.popleft()                #  a
# print(que)
# que.popleft()                #  b
# print(que)
