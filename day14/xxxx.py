#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: xxxx.py
# @Author: dell
# @Date: 2020/10/22  17:29
# @Desc: 
# @Project: licode
# @Source: PyCharm
import re
from copy import deepcopy

data = """
[root@dcdf536a-6130-543d-8f6b-c2ae30d1b133 chenhui]# df -h | grep chenhui
/dev/sdk               2.0T   20G  2.0T   1% /root/chenhui
[root@dcdf536a-6130-543d-8f6b-c2ae30d1b133 chenhui]#
"""

# data = data.replace("\n", "")
#
# re_comp = re.compile(r"sd[a-z]")
#
# re_split_result = re_comp.findall(data)
#
# print(re_split_result)

data_split = data.split("\n")

copy_data_split = deepcopy(data_split)

for i in range(len(data_split)):
    if not data_split[i]:
        copy_data_split.remove(data_split[i])
#
if len(copy_data_split) >= 3:
    copy_data_split = copy_data_split[1:-1]

print(copy_data_split)
