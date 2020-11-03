#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: set_demo.py
# @Author: dell
# @Date: 2020/11/3  14:00
# @Desc: 
# @Project: licode
# @Source: PyCharm


nic_list = [1, 2, 3]

used_nic = [2, 3]

print(list(set(nic_list).difference(set(used_nic))))

