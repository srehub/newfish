#!/usr/bin/python
# encoding:utf-8

"""
@author: yuanxin
contact:
@file: 2017/9/6-sophia_python.py
@time: 2017/9/6 
"""

import ibtisam as mom
import boaz as dad

class Sophia(mom.genes, dad.genes):
    """
    Welcome home
    """

    def __init__(self):
        print("Welcome to our home!")

    def live(self):
        while True:
            self.go_to_sleep()
            yield Bardak()
            self.be_awesome()

    def be_awesome(self):
        # Nothing to do.. already awesone
        print("Nothing to do.. already awesone")

if __name__=='__main__':
    baby = Sophia()
    boy =Sophia.be_awesome('a')
