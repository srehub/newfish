#!/usr/bin/python
# encoding:utf-8

"""
@author: yuanxin
contact:
@file: 2017/8/17-get-img-update.py
@time: 2017/8/17
"""

import requests
import re
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
r = requests.get(url='https://www.baidu.com')
# print(r.text)
res = r.text

pattern = r"www.baidu.com.*logo.*(png|jnp)"
m = re.search(pattern, res )    #  这里是怎么匹配到 logo1 的呢？
if m:
    print('01' , m.group(0))

imgurl = 'http://'+m.group(0)
print('02',imgurl)
response = requests.get(imgurl)
print(response.status_code)
print('03',imgurl)
resurl = requests.get(imgurl)
file = open(imgurl.split('/')[-1],'wb')
print('05',file)
file.write(resurl.content)
file.close()