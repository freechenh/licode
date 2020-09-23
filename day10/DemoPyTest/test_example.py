#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: test_example.py
# @Author: dell
# @Date: 2019/12/26
# @Desc: 
# @Project: bugQuery
# @Source: PyCharm
# import pytest


def inc(x):
    return x + 1


def test_answer(demo_fixture):
    # print(demo_fixture)
    assert inc(3) == 5
