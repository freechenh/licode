#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: query.py
# @Author: dell
# @Date: 2021/1/18  16:02
# @Desc: 
# @Project: licode
# @Source: PyCharm


import requests


def get_cartoon_characters(name):
    # pact作为模拟生产者时，其端口默认为1234
    resp = requests.get('http://localhost:1234/information', {'name': name})
    return resp
