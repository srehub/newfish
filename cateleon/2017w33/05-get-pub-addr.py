#!/usr/bin/python
# encoding:utf-8

"""
@author: yuanxin
contact:
@file: 2017/8/19-05-get-pub-addr.py
@time: 2017/8/19 
"""

import re
import urllib
class getPubIP:
    def getIP(self):
        try:
            myIP = self.visit("http://ip.chinaz.com/getip.aspx")
        except:
            try:
                myIP = self.visit("http://ipv4.icanhazip.com/")
            except:
                myIP = "So sorry!!! I can't get you public ipaddr. "
        return myIP
    def visit(self,url):
        opener = urllib.urlopen(url)
        if url == opener.read():
            str = opener.read()
        return re.search('\d+\.\d+\.\d+\.\d+', str).group(0)

if __name__=="__main__":
    getMyIP = getPubIP()
    print(getMyIP.getIP())