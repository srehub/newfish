#!/usr/bin/python
# encoding:utf-8

"""
@author: yuanxin
contact:
@file: 2017/9/17-most_starts_in_github.py
@time: 2017/9/17 
"""

"""
开始挖掘数据
"""

import requests
import time

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# print(dir(requests))
req = requests.get(url)
# print(dir(req))
print("Requests code:", req.status_code)     # 打印返回码

response_dict = req.json()
# print(response_dict.keys())
localtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print("Now the time is: ", localtime)        # 打印当前时间
print("There's Total repositories on GitHub: ", response_dict['total_count'])
# 统计当前 Github 上的 python repositories 总数量

repo_dicts = response_dict['items']
print("Repositories returned: ", len(repo_dicts))

# 开始研究第一个 repositories ； 包含多少 keys
repo_dict = repo_dicts[0]
print("\nKeys: ", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)