#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: xxxx.py
# @Author: dell
# @Date: 2020/12/29  17:34
# @Desc: 
# @Project: licode
# @Source: PyCharm


a = [{
    'id': '27c0d840-f617-4fa3-a24c-2b4696922b3b',
    'label': 'eno1'
},
    {
        'id': '4836aec1-cbfc-46e1-bea9-c73b38269184',
        'label': 'enp4s0f1'
    }]

b = [{
    "id": "27c0d840-f617-4fa3-a24c-2b4696922b3b",
    "label": "eno1"
}]

for i in b:
    assert i in a
