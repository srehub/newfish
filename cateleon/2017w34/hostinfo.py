#!/usr/bin/python
# encoding:utf-8

"""
@author: yuanxin
contact:
@file: 2017-8-21-hostinfo.py
@time: 2017-8-21 
"""

"""
可以查询主机信息的python模块
"""

import os
import sys
import shutil
import json
import tabulate
import pprint

host = sys.argv[1]
tmp_dir = 'tmp_fact_col'

try:
    shutil.rmtree(tmp_dir)
except OSError:
    pass
os.mkdir(tmp_dir)
cmd = "ansible -t {} -m setup {} >/dev/null".format(tmp_dir, host)
os.system(cmd)

headers = [
    'Name', 'FQDN', 'Datetime', 'OS', 'Arch', 'Mem', 'Disk', 'Diskfree', 'IPs',
]
d = []

for fname in os.listdir(tmp_dir):
    path = os.path.join(tmp_dir, fname)
    j = json.load(file(path, 'r'))
    if 'failed' in j:
        continue
    d.append(
        (
            fname,
            j['ansible_facts']['ansible_fqdn'],
            "%s %s:%s %s %s" % (
                j['ansible_facts']['ansible_date_time']['date'],
                j['ansible_facts']['ansible_date_time']['hour'],
                j['ansible_facts']['ansible_date_time']['minute'],
                j['ansible_facts']['ansible_date_time']['tz'],
                j['ansible_facts']['ansible_date_time']['tz_offset'],
            ),
            "%s %s" % (
                j['ansible_facts']['ansible_distribution'],
                j['ansible_facts']['ansible_distribution_version'],
            ),
            j['ansible_facts']['ansible_architecture'],
            '%0.fg (free %0.2fg)' % (
                (j['ansible_facts']['ansible_memtotal_mb'] / 1000.0),
                (j['ansible_facts']['ansible_memfree_mb'] / 1000.0)
                ),
            ', '.join([str(i['size_total']/1048576000) + 'g' for i in j['ansible_facts']['ansible_mounts']]),
            ', '.join([str(i['size_available']/1048576000) + 'g' for i in j['ansible_facts']['ansible_mounts']]),
            ', '.join(j['ansible_facts']['ansible_all_ipv4_addresses']),
        )
    )
    os.unlink(path)
shutil.rmtree(tmp_dir)
print(tabulate.tabulate(d, headers=headers))