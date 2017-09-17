#!/usr/bin/python
# encoding:utf-8

"""
@author: yuanxin
contact:
@file: 2017/9/17-most_starts_in_github.py
@time: 2017/9/17 
"""

"""
开始分析第一个仓库
"""

import requests
import time

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
req = requests.get(url)

response_dict = req.json()
localtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print("Now the time is: ", localtime)        # 打印当前时间
print("There's Total repositories on GitHub: ", response_dict['total_count'])
# 统计当前 Github 上的 python repositories 总数量

repo_dicts = response_dict['items']
print("Repositories returned: ", len(repo_dicts))

# 开始研究第一个 repositories ； 包含多少 keys
for repo_dict in repo_dicts:
    print("\nSelectd information about first repository: ")
    print('Name:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Created:', repo_dict['created_at'])
    print('Updated:', repo_dict['updated_at'])
    print('Description:', repo_dict['description'])