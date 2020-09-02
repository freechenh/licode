#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: re_demo.py
# @Author: dell
# @Date: 2020/9/2  14:44
# @Desc: 
# @Project: licode
# @Source: PyCharm


import re


p = re.compile(r"\[root.*?\]#")


text = """Ordinary users do not have access to the system

Last login: Wed Sep  2 14:37:07 2020 from 172.20.113.56

[root@db054e50-47c6-5f74-ae56-2809db44c737 ~]# cksum /home/gejian/test2.log | aw 
k '{print $1}'
3461083091
[root@db054e50-47c6-5f74-ae56-2809db44c737 ~]# """


print(p.findall(text))

print(p.search(text).group(), p.search(text))

print(p.match(text))
