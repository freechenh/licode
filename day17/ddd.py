#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: ddd.py
# @Author: dell
# @Date: 2020/11/3  11:16
# @Desc: 
# @Project: licode
# @Source: PyCharm
from jsonpath import jsonpath

demo = {"content": {"nicArr": [
    {"address": "", "gateway": "", "mac": "6c:92:bf:0f:95:c4", "model": "I350 Gigabit Network Connection",
     "name": "eno1", "netmask": "", "nicType": "TP", "speed": "1000", "status": "UP"},
    {"address": "", "gateway": "", "mac": "6c:92:bf:0f:95:c5", "model": "I350 Gigabit Network Connection",
     "name": "enp4s0f1", "netmask": "", "nicType": "TP", "speed": "10", "status": "UP"}]}, "message": None,
        "msgArgArr": None, "msgKey": None, "status": "SUCCESS"}

demo_a = jsonpath(demo, "$..name")

print(demo_a)

# result = []
#
# for i in demo_a:
#     if i:
#         result += i
#
# print(result)
