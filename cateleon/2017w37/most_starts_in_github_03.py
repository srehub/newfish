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
import pygal
from pygal.style import LightColorizedStyle as LCS, LightStyle as LS
import time

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
req = requests.get(url)
print("Request Code: ", req.status_code)

response_dict = req.json()
localtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print("Now the time is: ", localtime)        # 打印当前时间
print("There's Total repositories on GitHub: ", response_dict['total_count'])
# 统计当前 Github 上的 python repositories 总数量
repo_dicts = response_dict['items']

names,stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# pygal 可视化
my_style = LS('#333366', base_style=LCS)
# my_style = LS(base_style=LCS)
# chart = pygal.Bar(style=my_style, x_label_rotation=45 )
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = '最受欢迎的 Python 项目'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svg')