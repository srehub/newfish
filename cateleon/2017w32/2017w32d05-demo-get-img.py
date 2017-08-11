#!/usr/bin/python
# encoding:utf-8

"""
@author: yuanxin
contact:
@file: 2017/8/12-get-img.py
@time: 2017/8/12 
"""

import requests

url = "http://www.baidu.com"
response = requests.get(url)
print(response.status_code)
print(response.text)

imgurl = "http://www.baidu.com/img/bd_logo1.png"
resurl = requests.get(imgurl)
file = open(imgurl.split('/')[-1],'wb')
file.write(resurl.content)
file.close()