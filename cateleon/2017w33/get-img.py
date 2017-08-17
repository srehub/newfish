#!/usr/bin/python
# encoding:utf-8

"""
@author: yuanxin
contact:
@file: 2017/8/12-get-img.py
@time: 2017/8/12 
"""

import requests
import re
url = "http://www.baidu.com"
response = requests.get(url)
# print(response.status_code)
# print(response.content)
# urlcontent = response.content
# urlcontent = print(response.content)
# print(re.findall('bd_logo1.png', urlcontent )
# imgPath = re.findall('bd_logo', 'www.baidu.com/img/bd_logo1.png' )
# print(imgPath)
# imgfile = open()
bd = open('baidu.txt')
bdtxt = bd.read()
# print(bdtxt)
imgurl = re.findall('www.baidu.com/img/bd_logo1\.png|\.img', bdtxt )
imgurl2 = re.findall('www.baidu.com/img/bd_logo1.png' , bdtxt)
print('01',imgurl)
print('02',imgurl2)
# outfile.write(urlout.content)
bd.close()

bdurl = "http://www.baidu.com/img/"+str(imgurl[0])
# bdurl = imgurl2
# print('04',bdurl[0])
response = requests.get(bdurl)
print(response.status_code)
print('03',bdurl)
resurl = requests.get(bdurl)
file = open(bdurl.split('/')[-1],'wb')
print('05',file)
file.write(resurl.content)
file.close()