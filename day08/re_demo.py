#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: re_demo.py
# @Author: dell
# @Date: 2020/9/3  10:47
# @Desc: 
# @Project: licode
# @Source: PyCharm


import re

text = """Ordinary users do not have access to the system

Last login: Thu Sep  3 10:52:19 2020 from 172.20.113.56

[root@2a027a1e-1365-5fd2-b1e9-cab11f432713 ~]# ipmitool lan print 1 | grep 'IP A 
ddress' | grep -v 'IP Address Source' | awk '{print $4}'

You have new mail in /var/spool/mail/root
[root@2a027a1e-1365-5fd2-b1e9-cab11f432713 ~]# 
"""

pat = re.compile(r"(\d{0,3}\.\d{0,3}\.\d{0,3}\.\d{0,3})")

if pat.search(text):
    print(pat.findall(text))
else:
    print(None)
