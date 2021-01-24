#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: conftest.py
# @Author: dell
# @Date: 2020/7/6  19:21
# @Desc: 
# @Project: bugQuery
# @Source: PyCharm
import pytest

seq = ["case1", "case2", "case3"]

ddd = ['case']

dddd = [{"a": "b", "v": 1}]


@pytest.fixture(scope='class', params=seq)
def demo_fixture(request):
    print('前置条件')
    print(request.param['a'])
    return 'chenhui'


@pytest.fixture(scope="module", params=seq)
def params(request):
    return request.param


@pytest.fixture(scope='class')
def demo_a():
    print("前置条件")
    yield
    print("后置条件")
